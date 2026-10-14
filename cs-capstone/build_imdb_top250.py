#!/usr/bin/env python3
"""
Build a Top-250 SQLite DB from the IMDb datasets, the pasted chart text, and the pasted chart links.

    python build_imdb_top250.py --chart top250.txt --links links.txt --out movies.db
    python build_imdb_top250.py ... --birth-year-fallback

Needs in --data-dir: name.basics, title.basics, title.crew, title.principals (.tsv.gz)
"""

import argparse, csv, gzip, json, os, re, sqlite3, sys

csv.field_size_limit(sys.maxsize)

SCHEMA = """
CREATE TABLE movie (
  id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, runtime INTEGER,
  content_rating TEXT, imdb_rank INTEGER
);
CREATE TABLE genre (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE);
CREATE TABLE movie_genre (
  movie_id INTEGER NOT NULL REFERENCES movie(id),
  genre_id INTEGER NOT NULL REFERENCES genre(id),
  PRIMARY KEY (movie_id, genre_id)
);
CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT NOT NULL, birth_date TEXT);
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

CAST_CATEGORIES = {"actor", "actress", "self"}
META = re.compile(r"^(\d{4})(?:(\d+)h)?\s*(?:(\d+)m)?\s*(.*)$")


def num(imdb_id):  # 'tt0111161' -> 111161
    return int(imdb_id[2:])


def nul(v):
    return None if v == r"\N" else v


def read_tsv(path):
    with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
        yield from csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE)


def parse_chart(path):
    """Pasted chart text: '#N', title line, then 'YYYY<runtime><rating>' (rating may be empty)."""
    text = open(path, encoding="utf-8").read()
    parts = re.split(r"(?m)^#(\d+)\s*$", text)
    out = {}
    for rank, body in zip(parts[1::2], parts[2::2]):
        lines = [l.strip() for l in body.splitlines() if l.strip()]
        m = META.match(lines[1])
        if not m:
            raise ValueError(f"cannot parse meta line for #{rank}: {lines[1]!r}")
        year, h, mi, rating = m.groups()
        out[int(rank)] = dict(
            title=lines[0],
            year=int(year),
            runtime=(int(h or 0) * 60 + int(mi or 0)) or None,
            rating=rating.strip() or None,
        )
    return out


def parse_links(path):
    """Rank from ref_=chttp_t_N, falling back to line order."""
    out = {}
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        t = re.search(r"tt\d+", line)
        if not t:
            continue
        r = re.search(r"chttp_t_(\d+)", line)
        out[int(r.group(1)) if r else i] = t.group(0)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chart", required=True, help="pasted text of the chart page")
    ap.add_argument(
        "--links", required=True, help="one imdb.com/title/tt... URL per line"
    )
    ap.add_argument("--out", default="movies.db")
    ap.add_argument("--data-dir", default=".")
    ap.add_argument(
        "--birth-year-fallback",
        action="store_true",
        help="store birthYear ('1952') in birth_date; default leaves it NULL",
    )
    a = ap.parse_args()
    p = lambda n: os.path.join(a.data_dir, n)

    chart, links = parse_chart(a.chart), parse_links(a.links)
    if set(chart) != set(links):
        print(
            "WARNING: ranks differ between chart and links:",
            sorted(set(chart) ^ set(links))[:10],
        )
    entries = {}  # tconst -> merged entry
    for rank in sorted(set(chart) & set(links)):
        entries[links[rank]] = dict(chart[rank], rank=rank)
    print(f"{len(entries)} movies")

    if os.path.exists(a.out):
        os.remove(a.out)
    db = sqlite3.connect(a.out)
    db.executescript(SCHEMA)

    # movie + genre. Title/rank/rating from the chart; runtime/genres from basics.
    genre_ids, seen = {}, set()
    for r in read_tsv(p("title.basics.tsv.gz")):
        e = entries.get(r["tconst"])
        if not e:
            continue
        seen.add(r["tconst"])
        sy = nul(r["startYear"])
        if sy and int(sy) != e["year"]:
            print(
                f"WARNING: #{e['rank']} {e['title']!r}: chart year {e['year']} "
                f"!= dataset {sy} ({r['tconst']}) - check the link/rank alignment"
            )
        rt = nul(r["runtimeMinutes"])
        db.execute(
            "INSERT INTO movie VALUES (?,?,?,?,?,?)",
            (
                num(r["tconst"]),
                e["title"],
                e["year"],
                int(rt) if rt else e["runtime"],
                e["rating"],
                e["rank"],
            ),
        )
        g = nul(r["genres"])
        for name in g.split(",") if g else []:
            if name not in genre_ids:
                genre_ids[name] = len(genre_ids) + 1
                db.execute("INSERT INTO genre VALUES (?,?)", (genre_ids[name], name))
            db.execute(
                "INSERT OR IGNORE INTO movie_genre VALUES (?,?)",
                (num(r["tconst"]), genre_ids[name]),
            )
    for t in sorted(set(entries) - seen):
        print(
            f"WARNING: {t} (#{entries[t]['rank']} {entries[t]['title']}) "
            f"not in title.basics - dataset snapshot too old? Row skipped."
        )

    # directors (title.crew) and cast roles (title.principals)
    dir_pairs = set()
    for r in read_tsv(p("title.crew.tsv.gz")):
        if r["tconst"] in seen:
            d = nul(r["directors"])
            for nm in d.split(",") if d else []:
                dir_pairs.add((r["tconst"], nm))

    people = {nm for _, nm in dir_pairs}
    role_rows = []
    for r in read_tsv(p("title.principals.tsv.gz")):
        if r["tconst"] in seen and r["category"] in CAST_CATEGORIES:
            people.add(r["nconst"])
            chars = nul(r["characters"])
            for c in json.loads(chars) if chars else [None]:
                role_rows.append((r["tconst"], r["nconst"], c))

    for r in read_tsv(p("name.basics.tsv.gz")):
        if r["nconst"] in people:
            by = nul(r["birthYear"])
            db.execute(
                "INSERT INTO person VALUES (?,?,?)",
                (
                    num(r["nconst"]),
                    r["primaryName"],
                    by if (a.birth_year_fallback and by) else None,
                ),
            )

    for t, nm in sorted(dir_pairs):
        db.execute("INSERT INTO director VALUES (?,?)", (num(t), num(nm)))
    for t, nm, c in role_rows:
        db.execute(
            "INSERT INTO role (movie_id, person_id, role_name) VALUES (?,?,?)",
            (num(t), num(nm), c),
        )

    db.commit()
    for tbl in ("movie", "genre", "movie_genre", "person", "director", "role"):
        print(f"{tbl:12s} {db.execute(f'SELECT COUNT(*) FROM {tbl}').fetchone()[0]}")
    db.close()


if __name__ == "__main__":
    main()
