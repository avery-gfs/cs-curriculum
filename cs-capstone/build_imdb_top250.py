#!/usr/bin/env python3
"""
Build movies.db (IMDb Top 250) from the IMDb datasets. Just run:  python build_imdb_top250.py

Inputs (current directory):
  links.txt   required: one imdb.com/title/tt... URL per line (rank from ref_=chttp_t_N)
  *.tsv.gz    name.basics, title.basics, title.crew, title.principals
              (any missing file is downloaded automatically)

All ids start at 1: movie.id = chart rank, person and genre ordered by name,
role ordered by movie then billing.
"""

import csv, gzip, json, os, re, sqlite3, sys, time, urllib.request

csv.field_size_limit(sys.maxsize)

DATA_DIR = "."
OUT_DB = "movies.db"
LINKS_FILE = "links.txt"
DATASET_BASE = "https://datasets.imdbws.com/"
DATASETS = [
    "name.basics.tsv.gz",
    "title.basics.tsv.gz",
    "title.crew.tsv.gz",
    "title.principals.tsv.gz",
]
CAST_CATEGORIES = {"actor", "actress", "self"}
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

SCHEMA = """
CREATE TABLE movie (
  id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, runtime INTEGER,
  imdb_rank INTEGER
);
CREATE TABLE genre (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE);
CREATE TABLE movie_genre (
  movie_id INTEGER NOT NULL REFERENCES movie(id),
  genre_id INTEGER NOT NULL REFERENCES genre(id),
  PRIMARY KEY (movie_id, genre_id)
);
CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT NOT NULL, birth_year INTEGER);
CREATE TABLE director (
  movie_id INTEGER NOT NULL REFERENCES movie(id),
  person_id INTEGER NOT NULL REFERENCES person(id),
  PRIMARY KEY (movie_id, person_id)
);
CREATE TABLE role (
  id INTEGER PRIMARY KEY,
  movie_id INTEGER NOT NULL REFERENCES movie(id),
  person_id INTEGER NOT NULL REFERENCES person(id),
  role_name TEXT
);
"""


# ------------------------------------------------------------------ progress
class Bar:
    def __init__(self, label):
        self.label, self.last = label, 0.0

    def show(self, frac, detail=""):
        now = time.time()
        if now - self.last < 0.1 and frac < 1:
            return
        self.last = now
        frac = max(0.0, min(1.0, frac))
        filled = int(frac * 24)
        sys.stdout.write(
            f"\r  {self.label:<22} [{'#' * filled}{'.' * (24 - filled)}] "
            f"{frac * 100:5.1f}% {detail:<22}"
        )
        sys.stdout.flush()

    def done(self, detail=""):
        self.last = 0
        self.show(1.0, detail)
        sys.stdout.write("\n")


def mb(n):
    return f"{n / 1e6:.0f} MB"


# ----------------------------------------------------------------- datasets
def ensure_datasets():
    missing = [n for n in DATASETS if not os.path.exists(os.path.join(DATA_DIR, n))]
    if not missing:
        print("  dataset files found, skipping download")
        return
    print(f"  downloading {len(missing)} missing file(s)")
    for name in missing:
        path = os.path.join(DATA_DIR, name)
        part = path + ".part"
        req = urllib.request.Request(DATASET_BASE + name, headers={"User-Agent": UA})
        bar = Bar(name)
        try:
            with (
                urllib.request.urlopen(req, timeout=60) as resp,
                open(part, "wb") as out,
            ):
                total = int(resp.headers.get("Content-Length") or 0)
                got = 0
                while chunk := resp.read(1 << 20):
                    out.write(chunk)
                    got += len(chunk)
                    bar.show(
                        got / total if total else 0,
                        f"{mb(got)}/{mb(total)}" if total else mb(got),
                    )
            os.replace(part, path)
            bar.done(mb(got))
        except Exception as ex:
            if os.path.exists(part):
                os.remove(part)
            sys.exit(f"\nDownload of {name} failed: {ex}")


def read_tsv(name, label):
    path = os.path.join(DATA_DIR, name)
    size = os.path.getsize(path)
    bar = Bar(label)
    i = -1
    with open(path, "rb") as raw:
        with gzip.open(raw, "rt", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
            for i, row in enumerate(reader):
                if i % 20000 == 0:
                    bar.show(raw.tell() / size, f"{i:,} rows")
                yield row
            bar.done(f"{i + 1:,} rows")


def nul(v):
    return None if v == r"\N" else v


# ------------------------------------------------------------------- links
def load_links():
    if not os.path.exists(LINKS_FILE):
        sys.exit(
            f"{LINKS_FILE} not found. Put one imdb.com/title/tt... URL per line "
            f"in this folder."
        )
    entries, seen = [], set()
    for i, line in enumerate(open(LINKS_FILE, encoding="utf-8"), 1):
        t = re.search(r"tt\d+", line)
        if not t:
            continue
        r = re.search(r"chttp_t_(\d+)", line)
        rank = int(r.group(1)) if r else i
        if t.group(0) in seen:
            print(f"  WARNING: duplicate id {t.group(0)} on line {i}, ignored")
            continue
        seen.add(t.group(0))
        entries.append(dict(rank=rank, tconst=t.group(0)))
    if not entries:
        sys.exit(f"No tt ids found in {LINKS_FILE}.")
    entries.sort(key=lambda e: e["rank"])
    for i, e in enumerate(entries, 1):  # ranks exactly 1..N, in link order
        e["rank"] = i
    return entries


# --------------------------------------------------------------------- main
def main():
    print("[1/6] Dataset files")
    ensure_datasets()

    print("[2/6] Reading list")
    entries = load_links()
    by_t = {e["tconst"]: e for e in entries}
    print(f"  {len(entries)} movies from {LINKS_FILE}")

    print("[3/6] Reading dataset files")
    basics = {}  # tconst -> (primaryTitle, year, runtime, genres)
    for r in read_tsv("title.basics.tsv.gz", "title.basics"):
        if r["tconst"] in by_t:
            sy, rt, g = nul(r["startYear"]), nul(r["runtimeMinutes"]), nul(r["genres"])
            basics[r["tconst"]] = (
                r["primaryTitle"],
                int(sy) if sy else None,
                int(rt) if rt else None,
                g.split(",") if g else [],
            )
    kept = {}
    for t, e in by_t.items():
        if t not in basics:
            print(
                f"  WARNING: #{e['rank']} ({t}) not in title.basics "
                f"(dataset older than the list?). Skipped."
            )
            continue
        kept[t] = e

    dir_pairs = set()
    for r in read_tsv("title.crew.tsv.gz", "title.crew"):
        if r["tconst"] in kept:
            d = nul(r["directors"])
            for nm in d.split(",") if d else []:
                dir_pairs.add((r["tconst"], nm))

    people = {nm for _, nm in dir_pairs}
    role_rows = []  # (rank, billing order, nconst, character)
    for r in read_tsv("title.principals.tsv.gz", "title.principals"):
        if r["tconst"] in kept and r["category"] in CAST_CATEGORIES:
            people.add(r["nconst"])
            chars = nul(r["characters"])
            for c in json.loads(chars) if chars else [None]:
                role_rows.append((
                    kept[r["tconst"]]["rank"],
                    int(r["ordering"]),
                    r["nconst"],
                    c,
                ))

    plist = []
    for r in read_tsv("name.basics.tsv.gz", "name.basics"):
        if r["nconst"] in people:
            by = nul(r["birthYear"])
            plist.append((r["primaryName"], r["nconst"], int(by) if by else None))
    plist.sort()
    pid = {nconst: i for i, (_, nconst, _) in enumerate(plist, 1)}

    print("[4/6] Writing database")
    tmp = OUT_DB + ".tmp"
    for f in (tmp, tmp + "-journal"):
        if os.path.exists(f):
            os.remove(f)
    db = sqlite3.connect(tmp)
    db.executescript(SCHEMA)

    gid = {
        n: i for i, n in enumerate(sorted({g for t in kept for g in basics[t][3]}), 1)
    }
    db.executemany("INSERT INTO genre VALUES (?,?)", [(i, n) for n, i in gid.items()])

    bar = Bar("movies")
    ordered = sorted(kept.items(), key=lambda kv: kv[1]["rank"])
    for k, (t, e) in enumerate(ordered, 1):
        title, year, runtime, genres = basics[t]
        db.execute(
            "INSERT INTO movie VALUES (?,?,?,?,?)",
            (e["rank"], title, year, runtime, e["rank"]),
        )
        for g in genres:
            db.execute("INSERT INTO movie_genre VALUES (?,?)", (e["rank"], gid[g]))
        bar.show(k / len(ordered), f"{k}/{len(ordered)}")
    bar.done(f"{len(ordered)}/{len(ordered)}")

    bar = Bar("people")
    db.executemany(
        "INSERT INTO person VALUES (?,?,?)",
        [(i, name, by) for i, (name, _, by) in enumerate(plist, 1)],
    )
    bar.done(f"{len(plist):,}")

    bar = Bar("directors and roles")
    dir_sorted = sorted(dir_pairs, key=lambda x: (kept[x[0]]["rank"], pid[x[1]]))
    role_sorted = sorted(role_rows, key=lambda x: (x[0], x[1], x[2], x[3] or ""))
    total = len(dir_sorted) + len(role_sorted)
    n = 0
    for t, nm in dir_sorted:
        db.execute("INSERT INTO director VALUES (?,?)", (kept[t]["rank"], pid[nm]))
        n += 1
        if n % 500 == 0:
            bar.show(n / total, f"{n:,}/{total:,}")
    for rank, _, nm, c in role_sorted:
        db.execute(
            "INSERT INTO role (movie_id, person_id, role_name) VALUES (?,?,?)",
            (rank, pid[nm], c),
        )
        n += 1
        if n % 500 == 0:
            bar.show(n / total, f"{n:,}/{total:,}")
    bar.done(f"{total:,}")

    print("[5/6] Verifying")
    db.commit()
    assert db.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
    assert not db.execute("PRAGMA foreign_key_check").fetchall(), (
        "foreign key violation"
    )
    for tbl in ("movie", "genre", "movie_genre", "person", "director", "role"):
        print(
            f"  {tbl:12s} {db.execute(f'SELECT COUNT(*) FROM {tbl}').fetchone()[0]:,}"
        )
    db.close()

    print("[6/6] Finalizing")
    os.replace(tmp, OUT_DB)
    print(f"Done: {OUT_DB}")


if __name__ == "__main__":
    main()
