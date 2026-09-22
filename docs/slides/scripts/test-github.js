// Checks the pure parts of app/github.js — source parsing, link rewriting and
// the deck listing — without a browser: node scripts/test-github.js
import assert from "node:assert/strict";
import {
  deckPaths,
  labelledSlideIndexes,
  parseSource,
  prepareMarkdown,
  splitSlides,
  splitTitle,
} from "../app/github.js";

const CLASS = { owner: "avery-gfs", repo: "classes-26", ref: "solutions" };
let ran = 0;

function test(name, fn) {
  ran++;
  try {
    fn();
  } catch (err) {
    console.error(`FAIL  ${name}\n${err.message}\n`);
    process.exitCode = 1;
  }
}

// -- parseSource -------------------------------------------------------------

test("a bare path means the class repo", () => {
  assert.deepEqual(parseSource("cs-1/00-introduction"), {
    ...CLASS,
    path: "cs-1/00-introduction",
  });
  assert.deepEqual(parseSource("/cs-1/00-introduction/readme.md"), {
    ...CLASS,
    path: "cs-1/00-introduction/readme.md",
  });
});

test("blob and tree urls", () => {
  assert.deepEqual(
    parseSource("https://github.com/owner/repo/blob/main/docs/README.md"),
    { owner: "owner", repo: "repo", ref: "main", path: "docs/README.md" },
  );
  assert.deepEqual(parseSource("https://github.com/owner/repo/tree/v2/docs"), {
    owner: "owner",
    repo: "repo",
    ref: "v2",
    path: "docs",
  });
});

test("a bare repo url uses HEAD", () => {
  assert.deepEqual(parseSource("github.com/owner/repo"), {
    owner: "owner",
    repo: "repo",
    ref: "HEAD",
    path: "",
  });
});

test("raw urls, including the refs/heads form", () => {
  assert.deepEqual(
    parseSource(
      "https://raw.githubusercontent.com/o/r/refs/heads/my/branch/a/readme.md",
    ),
    { owner: "o", repo: "r", ref: "refs/heads/my", path: "branch/a/readme.md" },
  );
  assert.deepEqual(
    parseSource("https://raw.githubusercontent.com/o/r/main/a/readme.md"),
    { owner: "o", repo: "r", ref: "main", path: "a/readme.md" },
  );
});

test("percent-encoded segments are decoded", () => {
  assert.equal(
    parseSource("https://github.com/o/r/blob/main/my%20notes/readme.md").path,
    "my notes/readme.md",
  );
});

test("unusable input is rejected", () => {
  assert.throws(() => parseSource(""), /No source/);
  assert.throws(() => parseSource("https://gitlab.com/o/r"), /github\.com/);
  assert.throws(() => parseSource("https://github.com/o/r/issues/3"), /blob/);
});

// -- prepareMarkdown ---------------------------------------------------------

const at = { ...CLASS, path: "cs-1/00-introduction/readme.md" };
const raw = "https://raw.githubusercontent.com/avery-gfs/classes-26/solutions";

test("relative images become raw urls", () => {
  assert.equal(
    prepareMarkdown("![](assets/x.png)", at),
    `![](${raw}/cs-1/00-introduction/assets/x.png)`,
  );
  assert.equal(
    prepareMarkdown('<img src="assets/x.png" width="200">', at),
    `<img src="${raw}/cs-1/00-introduction/assets/x.png" width="200">`,
  );
});

test("../ walks up from the file's folder", () => {
  assert.equal(
    prepareMarkdown("![](../../assets/maze.png)", at),
    `![](${raw}/assets/maze.png)`,
  );
});

test("absolute urls and anchors are untouched", () => {
  const md = "![](https://example.com/a.png) [x](#section) [y](mailto:a@b.c)";
  assert.equal(prepareMarkdown(md, at), md);
});

test("links to markdown and folders open in the viewer", () => {
  const root = { ...CLASS, path: "readme.md" };
  assert.equal(
    prepareMarkdown("[CS 1](cs-1)", root),
    "[CS 1](view.html?src=cs-1)",
  );
  assert.equal(
    prepareMarkdown("[next](../01-variables/readme.md)", at),
    "[next](view.html?src=cs-1%2F01-variables%2Freadme.md)",
  );
});

test("links to other files open on github", () => {
  assert.equal(
    prepareMarkdown("[code](solution.py)", at),
    "[code](https://github.com/avery-gfs/classes-26/blob/solutions/cs-1/00-introduction/solution.py)",
  );
});

test("outside the class repo, links stay in that repo", () => {
  const other = { owner: "o", repo: "r", ref: "main", path: "docs/readme.md" };
  assert.equal(
    prepareMarkdown("![](img/a.png)", other),
    "![](https://raw.githubusercontent.com/o/r/main/docs/img/a.png)",
  );
  assert.equal(
    prepareMarkdown("[more](more.md)", other),
    "[more](view.html?src=https%3A%2F%2Fgithub.com%2Fo%2Fr%2Fblob%2Fmain%2Fdocs%2Fmore.md)",
  );
});

test("code is never rewritten", () => {
  const fenced = ["```py", 'print("![](a.png)")', "```", "", "![](a.png)"].join(
    "\n",
  );
  const out = prepareMarkdown(fenced, at);
  assert.match(out, /print\("!\[\]\(a\.png\)"\)/);
  assert.match(out, /!\[\]\(https:\/\/raw\./);
  assert.equal(
    prepareMarkdown("`[x](y.md)` and [x](y.md)", at).split("`")[1],
    "[x](y.md)",
  );
});

test("html comments are stripped", () => {
  assert.equal(prepareMarkdown("<!-- notes\nhere -->\n# Title", at), "# Title");
});

// -- splitSlides -------------------------------------------------------------

test("every `##` starts a slide", () => {
  assert.deepEqual(splitSlides("intro\n\n## One\n\na\n\n## Two\n\nb"), [
    "intro",
    "## One\n\na",
    "## Two\n\nb",
  ]);
});

test("`---` starts a slide that repeats the heading", () => {
  assert.deepEqual(
    splitSlides("## One\n\na\n\n---\n\nb\n\n---\n\nc\n\n## Two\n\nd"),
    [
      "## One\n\na",
      "## One\n\nb",
      "## One\n\nc",
      "## Two\n\nd",
    ],
  );
});

test("section indexes skip repeated slides and retain repeated heading labels", () => {
  assert.deepEqual(
    labelledSlideIndexes(
      "intro\n\n## One\n\na\n\n---\n\nb\n\n## One\n\nc\n\n...\n\nd",
    ),
    [1, 3],
  );
});

test("`---` before any heading just splits", () => {
  assert.deepEqual(splitSlides("a\n\n---\n\nb"), ["a", "b"]);
});

test("markers inside a code fence are left alone", () => {
  const md = "## One\n\n```\n---\n## not a heading\n```\n\ntail";
  assert.deepEqual(splitSlides(md), [md]);
});

test("a `---` with no blank line above it underlines the text, as in markdown", () => {
  const md = "## One\n\na\n---\n\nb";
  assert.deepEqual(splitSlides(md), [md]);
});

// -- splitTitle --------------------------------------------------------------

test("a lone title heading is lifted out, leaving no title slide", () => {
  assert.deepEqual(splitTitle("# Hello There\n\n## One\n\nbody"), {
    title: "Hello There",
    body: "## One\n\nbody",
  });
});

test("an introduction under the title stays as the first slide", () => {
  assert.deepEqual(splitTitle("# T\n\nIntro text.\n\n## One"), {
    title: "T",
    body: "Intro text.\n\n## One",
  });
});

test("badges above the title are kept, the title is still found", () => {
  assert.deepEqual(splitTitle("![badge](b.svg)\n\n# T\n\n## One"), {
    title: "T",
    body: "![badge](b.svg)\n\n## One",
  });
});

test("documents with no usable title are left alone", () => {
  const noHeading = "## One\n\nbody";
  assert.deepEqual(splitTitle(noHeading), { title: "", body: noHeading });

  // An `#` that only turns up after the first slide is a heading, not a title.
  const late = "## One\n\n# Later";
  assert.deepEqual(splitTitle(late), { title: "", body: late });

  // Nothing but a title still has to render as something.
  assert.deepEqual(splitTitle("# Only"), { title: "", body: "# Only" });
});

// -- deckPaths -------------------------------------------------------------

test("readmes plus top-level markdown, sorted naturally", () => {
  assert.deepEqual(
    deckPaths([
      "readme.md",
      "cs-1/00-introduction/readme.md",
      "cs-1/00-introduction/assets/x.png",
      "cs-1/01-variables-and-io/README.md",
      "cs-1/10-recursion/readme.md",
      "cs-1/2-loops/readme.md",
      "cs-1/notes.md",
      "sequence.md",
    ]),
    [
      "readme.md",
      "sequence.md",
      "cs-1/00-introduction/readme.md",
      "cs-1/01-variables-and-io/README.md",
      "cs-1/2-loops/readme.md",
      "cs-1/10-recursion/readme.md",
    ],
  );
});

if (!process.exitCode) console.log(`${ran} checks passed`);
