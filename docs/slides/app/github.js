// Everything that knows about GitHub: turning a user-supplied source into a
// {owner, repo, ref, path} location, fetching markdown over raw.githubusercontent,
// listing the class repo's readmes, and rewriting relative links inside a
// document so images and cross-references still resolve once the markdown has
// been lifted out of the repo.

export const CLASS_REPO = {
  owner: "avery-gfs",
  repo: "classes-26",
  ref: "public",
};

const RAW_HOST = "https://raw.githubusercontent.com";
const API_HOST = "https://api.github.com";

// -- locations ---------------------------------------------------------------

// raw.githubusercontent caches a *branch* URL for five minutes and nothing the
// client sends gets past it — not a query string, not `Cache-Control: no-cache`.
// A commit SHA is a different URL for every push, so once we know the head
// commit we read content from that instead and a push is visible immediately.
let commitPin = null;

export function rawUrl({ owner, repo, ref, path }) {
  const at = commitPin && isClassRepo({ owner, repo, ref }) ? commitPin : ref;
  return `${RAW_HOST}/${owner}/${repo}/${at}/${encodePath(path)}`;
}

export function blobUrl({ owner, repo, ref, path }) {
  const kind = path ? "blob" : "tree";
  return `https://github.com/${owner}/${repo}/${kind}/${ref}/${
    encodePath(path)
  }`;
}

export function treeUrl({ owner, repo, ref, path }) {
  return `https://github.com/${owner}/${repo}/tree/${ref}/${encodePath(path)}`;
}

export function isClassRepo(loc) {
  return (
    loc.owner === CLASS_REPO.owner &&
    loc.repo === CLASS_REPO.repo &&
    loc.ref === CLASS_REPO.ref
  );
}

// The shortest string that `parseSource` will turn back into this location.
export function sourceString(loc) {
  return isClassRepo(loc) ? loc.path : blobUrl(loc);
}

export function deckHref(loc) {
  return "view.html?src=" + encodeURIComponent(sourceString(loc));
}

function encodePath(path) {
  return String(path || "")
    .split("/")
    .map(encodeURIComponent)
    .join("/");
}

// -- parsing user input ------------------------------------------------------

export function parseSource(input) {
  let src = String(input || "").trim();
  if (/^<.*>$/s.test(src)) src = src.slice(1, -1).trim();
  if (!src) throw new Error("No source given.");

  if (/^https?:\/\//i.test(src)) return parseGitHubUrl(src);
  if (/^(www\.)?github\.com\//i.test(src)) {
    return parseGitHubUrl("https://" + src);
  }
  if (/^raw\.githubusercontent\.com\//i.test(src)) {
    return parseGitHubUrl("https://" + src);
  }
  if (/^[a-z][a-z0-9+.-]*:/i.test(src)) {
    throw new Error("Only github.com links are supported.");
  }

  // Anything else is read as a path inside the class repo.
  return { ...CLASS_REPO, path: normalizePath(src) };
}

function parseGitHubUrl(str) {
  let url;
  try {
    url = new URL(str);
  } catch {
    throw new Error(`Not a valid URL: ${str}`);
  }

  const host = url.hostname.toLowerCase().replace(/^www\./, "");
  const seg = url.pathname.split("/").filter(Boolean).map(safeDecode);

  if (host === "raw.githubusercontent.com") {
    const [owner, repo, ...rest] = seg;
    if (!owner || !repo) throw new Error(`Not a file link: ${str}`);
    return { owner, repo, ...splitRef(rest) };
  }

  if (host === "github.com") {
    const [owner, repo, kind, ...rest] = seg;
    if (!owner || !repo) throw new Error(`Not a repository link: ${str}`);
    if (!kind) return { owner, repo, ref: "HEAD", path: "" };
    if (!["blob", "tree", "raw", "blame"].includes(kind)) {
      throw new Error(
        `Link a file or folder in a repo (a /blob/ or /tree/ URL), not /${kind}/.`,
      );
    }
    return { owner, repo, ...splitRef(rest) };
  }

  throw new Error("Only github.com links are supported.");
}

// `rest` is everything after owner/repo/blob. The first segment is the ref,
// except for the fully-qualified `refs/heads/<branch>` form GitHub now emits.
// Branch names containing a slash are indistinguishable from paths here, so
// they only work in the `refs/heads/` form.
function splitRef(rest) {
  if (!rest.length) return { ref: "HEAD", path: "" };
  if (
    rest[0] === "refs" && ["heads", "tags"].includes(rest[1]) && rest.length > 2
  ) {
    return {
      ref: rest.slice(0, 3).join("/"),
      path: normalizePath(rest.slice(3).join("/")),
    };
  }
  return { ref: rest[0], path: normalizePath(rest.slice(1).join("/")) };
}

function safeDecode(s) {
  try {
    return decodeURIComponent(s);
  } catch {
    return s;
  }
}

export function normalizePath(path) {
  const out = [];
  for (const part of String(path || "").split("/")) {
    if (!part || part === ".") continue;
    if (part === "..") out.pop();
    else out.push(part);
  }
  return out.join("/");
}

export function dirOf(path) {
  const i = String(path || "").lastIndexOf("/");
  return i < 0 ? "" : path.slice(0, i);
}

function resolvePath(baseDir, rel) {
  if (rel.startsWith("/")) return normalizePath(rel);
  return normalizePath(baseDir ? `${baseDir}/${rel}` : rel);
}

// -- fetching ----------------------------------------------------------------

const README_NAMES = ["readme.md", "README.md", "Readme.md", "index.md"];
const MARKDOWN_RE = /\.(md|markdown|mdown|mkd)$/i;

export function isMarkdownPath(path) {
  return MARKDOWN_RE.test(path);
}

// Resolves a location that may point at a directory, and returns the markdown
// along with the location it actually came from (so relative links resolve
// against the file, not the folder the user typed).
export async function fetchMarkdown(loc) {
  let candidates;
  if (isMarkdownPath(loc.path)) {
    const dir = dirOf(loc.path);
    const base = loc.path.slice(dir ? dir.length + 1 : 0);
    // Casing is the usual reason a readme link 404s; try the other spellings.
    candidates = /^readme\.md$/i.test(base)
      ? README_NAMES.map((n) => (dir ? `${dir}/${n}` : n))
      : [loc.path];
  } else {
    candidates = README_NAMES.map((n) => (loc.path ? `${loc.path}/${n}` : n));
  }

  let status = 0;
  for (const path of candidates) {
    const at = { ...loc, path };
    let res;
    try {
      // raw.githubusercontent sends `max-age=300`, so without this the browser
      // serves a readme from its own disk cache for five minutes after a push
      // without ever asking. `no-cache` revalidates every time — unchanged
      // files still come back as a cheap 304.
      res = await fetch(rawUrl(at), { cache: "no-cache" });
    } catch (err) {
      throw new Error(`Could not reach GitHub (${err.message}).`);
    }
    if (res.ok) return { loc: at, text: await res.text() };
    status = res.status;
    if (status !== 404) break;
  }

  const where = `${loc.owner}/${loc.repo}@${loc.ref}/${loc.path}`;
  if (status === 404) {
    throw new Error(
      isMarkdownPath(loc.path)
        ? `No such file: ${where}`
        : `No readme.md found in ${where}`,
    );
  }
  throw new Error(`GitHub returned ${status} for ${where}`);
}

// -- link rewriting ----------------------------------------------------------

// Strips HTML comments and points every relative URL somewhere that works from
// this site: images at raw.githubusercontent, markdown at our own viewer, and
// anything else at the file's page on github.com.
export function prepareMarkdown(text, loc) {
  const stripped = text.replace(/<!--[\s\S]*?-->/g, "").trim();
  return outsideCode(stripped, (chunk) => rewriteLinks(chunk, loc));
}

// Runs `fn` over the parts of the markdown that aren't fenced blocks or inline
// code spans, so code samples are never touched.
function outsideCode(md, fn) {
  const fences = md.split(
    /(^ {0,3}(?:```|~~~)[\s\S]*?^ {0,3}(?:```|~~~)[^\n]*$)/gm,
  );
  return fences
    .map((part, i) => {
      if (i % 2) return part;
      return part
        .split(/(`+[^`]*`+)/g)
        .map((piece, j) => (j % 2 ? piece : fn(piece)))
        .join("");
    })
    .join("");
}

function rewriteLinks(text, loc) {
  return (
    text
      // ![alt](url "title") and [text](url "title")
      .replace(
        /(!?)\[([^\]]*)\]\(\s*<?([^)<>\s]*)>?(\s+["'][^)]*)?\)/g,
        (m, bang, label, url, title) =>
          `${bang}[${label}](${retarget(url, loc, bang ? "image" : "link")}${
            title || ""
          })`,
      )
      // [id]: url "title"
      .replace(
        /^( {0,3}\[[^\]]+\]:\s*)(\S+)/gm,
        (m, head, url) => head + retarget(url, loc, "link"),
      )
      // <img src="..."> / <source src="...">
      .replace(
        /(<(?:img|source|video|audio)\b[^>]*?\bsrc\s*=\s*)("[^"]*"|'[^']*')/gi,
        (m, head, quoted) =>
          head + requote(quoted, (u) => retarget(u, loc, "image")),
      )
      // <a href="...">
      .replace(
        /(<a\b[^>]*?\bhref\s*=\s*)("[^"]*"|'[^']*')/gi,
        (m, head, quoted) =>
          head + requote(quoted, (u) => retarget(u, loc, "link")),
      )
  );
}

function requote(quoted, fn) {
  const q = quoted[0];
  return q + fn(quoted.slice(1, -1)) + q;
}

function retarget(url, loc, kind) {
  const raw = String(url).trim();
  // Absolute, protocol-relative, in-page anchors and templating are left alone.
  if (!raw || /^([a-z][a-z0-9+.-]*:|\/\/|#|\{)/i.test(raw)) return url;

  const hash = raw.indexOf("#");
  const target = hash < 0 ? raw : raw.slice(0, hash);
  const frag = hash < 0 ? "" : raw.slice(hash);
  if (!target) return url;

  const at = { ...loc, path: resolvePath(dirOf(loc.path), target) };

  if (kind === "image") return rawUrl(at) + frag;
  // A markdown file, or a path with no extension (i.e. a folder with a readme),
  // is something this viewer can render itself.
  if (isMarkdownPath(at.path) || !/\.[a-z0-9]+$/i.test(at.path)) {
    return deckHref(at) + frag;
  }
  return blobUrl(at) + frag;
}

// -- listing the class repo --------------------------------------------------

const TREE_TTL_MS = 10 * 60 * 1000;

// The recursive tree API is one request for the whole repo, but unauthenticated
// callers get 60 requests an hour per IP — and a classroom shares one. So the
// result is cached, and a stale cache is preferred over an error.
export async function fetchTree(repo = CLASS_REPO, { force = false } = {}) {
  const key = `slides:tree:${repo.owner}/${repo.repo}@${repo.ref}`;
  const cached = readCache(key);
  if (!force && cached && Date.now() - cached.at < TREE_TTL_MS) {
    commitPin = cached.sha ?? null;
    return { ...cached, stale: false };
  }

  try {
    const url = `${API_HOST}/repos/${repo.owner}/${repo.repo}` +
      `/git/trees/${encodeURIComponent(repo.ref)}?recursive=1`;
    const res = await fetch(url, {
      headers: { Accept: "application/vnd.github+json" },
    });
    if (!res.ok) throw await apiError(res);

    const data = await res.json();
    const entry = {
      at: Date.now(),
      sha: data.sha,
      paths: data.tree.filter((e) => e.type === "blob").map((e) => e.path),
      truncated: !!data.truncated,
    };
    writeCache(key, entry);
    commitPin = entry.sha ?? null;
    return { ...entry, stale: false };
  } catch (err) {
    if (cached) return { ...cached, stale: true, error: err };
    throw err;
  }
}

// Resolves the class repo's head commit so decks are read from an immutable URL.
// A failure here is not worth reporting: without a pin the branch URL still
// works, it is just up to five minutes behind.
export async function pinToHead(options) {
  try {
    await fetchTree(CLASS_REPO, options);
  } catch {
    // Offline, or the API's hourly limit is used up.
  }
}

async function apiError(res) {
  if (res.status === 403 || res.status === 429) {
    if (res.headers.get("x-ratelimit-remaining") === "0") {
      const reset = Number(res.headers.get("x-ratelimit-reset")) * 1000;
      const at = reset ? new Date(reset).toLocaleTimeString() : "shortly";
      return new Error(
        `GitHub's hourly request limit for this network is used up (resets around ${at}). ` +
          `Slides themselves still open — it's only this list that needs the API.`,
      );
    }
  }
  if (res.status === 404) {
    return new Error(
      `No branch "${CLASS_REPO.ref}" in ${CLASS_REPO.owner}/${CLASS_REPO.repo}.`,
    );
  }
  return new Error(`GitHub returned ${res.status} listing the repository.`);
}

function readCache(key) {
  try {
    const raw = localStorage.getItem(key);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed.paths) ? parsed : null;
  } catch {
    return null;
  }
}

function writeCache(key, entry) {
  try {
    localStorage.setItem(key, JSON.stringify(entry));
  } catch {
    // Private browsing, full quota — the list just won't be cached.
  }
}

// -- deck listing ----------------------------------------------------------

// The markdown that gets a deck: every readme in the repo, plus any other
// top-level `.md` file. Sorted by path, with the repo-root files first.
export function deckPaths(paths) {
  return paths
    .filter((p) => /(^|\/)readme\.md$/i.test(p) || !p.includes("/"))
    .filter((p) => /\.md$/i.test(p))
    .sort((a, b) => {
      const rootA = !a.includes("/");
      const rootB = !b.includes("/");
      if (rootA !== rootB) return rootA ? -1 : 1;
      return a.localeCompare(b, undefined, { numeric: true });
    });
}

// -- slides ------------------------------------------------------------------

// Cuts a document into one string per slide. A `##` heading starts a new slide,
// and so does a `---` rule — which carries the heading it sits under along with
// it, so a run of them steps through one section a screenful at a time, each
// step replacing the last. Markers inside a fenced code block are left alone.
export function splitSlides(markdown) {
  const slides = [];
  let heading = ""; // the `##` line the slides in this section repeat
  let lines = [];
  let fence = "";
  // Whether the next line starts a block. A `---` that doesn't is a setext
  // heading underline, which is what markdown makes of it too.
  let open = true;

  const flush = () => {
    const body = lines.join("\n").replace(/^\n+/, "").replace(/\s+$/, "");
    const text = heading && body ? `${heading}\n\n${body}` : heading || body;
    if (text) slides.push(text);
    lines = [];
  };

  for (const line of String(markdown || "").split("\n")) {
    const token = /^ {0,3}(`{3,}|~{3,})/.exec(line)?.[1];

    if (fence) {
      if (token && token[0] === fence[0] && token.length >= fence.length) {
        fence = "";
      }
    } else if (token) {
      fence = token;
    } else if (/^##/.test(line)) {
      flush();
      heading = line;
      open = true;
      continue;
    } else if (open && /^ {0,3}-{3,}\s*$/.test(line)) {
      flush();
      continue;
    }

    lines.push(line);
    open = !fence && !line.trim();
  }

  flush();
  return slides;
}

// The document's `# Title` is the name of the whole deck, so it becomes a
// running header rather than a title slide of its own. Only the line itself is
// taken — badges or a language switcher above it, and any real introduction
// below it, stay behind as the first slide.
export function splitTitle(markdown) {
  const heading = /^ {0,3}#\s+(.+?)\s*#*\s*$/m.exec(markdown);
  const firstSlide = markdown.search(/^ {0,3}##\s/m);
  if (!heading || (firstSlide !== -1 && heading.index > firstSlide)) {
    return { title: "", body: markdown };
  }

  const title = heading[1].trim();
  const before = markdown.slice(0, heading.index).replace(/\n+$/, "");
  const after = markdown.slice(heading.index + heading[0].length).replace(
    /^\n+/,
    "",
  );
  let body = before ? `${before}\n\n${after}` : after;

  // Nothing but the title before the first `##` means there is no first slide.
  const preamble = body.split(/\n(?=##)/, 1)[0];
  if (!preamble.trim()) body = body.slice(preamble.length).replace(/^\n+/, "");

  // A document that is nothing but its title still needs one slide.
  return body.trim() ? { title, body } : { title: "", body: markdown };
}
