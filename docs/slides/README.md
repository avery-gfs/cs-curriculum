# Slides

Renders the readmes in
[avery-gfs/classes-26](https://github.com/avery-gfs/classes-26) as reveal.js
decks, entirely in the browser: markdown and images are fetched straight from
GitHub, with no server or build step.

Published at <https://avery-gfs.github.io/slides/>.

## Pages

- **`index.html`** lists every `readme.md` in the class repo (plus top-level
  `.md` files, minus `docs/`), each linking to its deck.
- **`view.html?src=…`** renders one document. `src` is a class-repo path or any
  GitHub file or folder URL; a folder resolves to its `readme.md`.

  ```
  view.html?src=cs-1/00-introduction
  view.html?src=https://github.com/owner/repo/blob/main/README.md
  ```

HTML comments are stripped. Relative links are rewritten: images to
`raw.githubusercontent.com`, markdown to this viewer, everything else to GitHub.
Only fences that name a language are highlighted; bare ``` blocks are treated as
program output and shown verbatim.

## Syntax

The `# heading` becomes a small running header on every slide; anything else
before the first `##` is the first slide. Each `##` starts a new slide, and
these markers (on their own line, blank lines around, ignored inside code
fences) control steps within it:

| Marker | Effect                                                                                                               |
| ------ | -------------------------------------------------------------------------------------------------------------------- |
| `---`  | New slide with the same heading, **replacing** what was shown.                                                       |
| `...`  | **Adds** the next block below as a fragment.                                                                         |
| `<<<`  | First one does nothing; each later one **erases back to the previous `<<<`**, keeping the setup above the first.     |
| `///`  | Splits the slide into **two columns**. Only the first per slide counts; it repeats with the `<<<` setup if above it. |

```
## Evaluating

f(2)

---

f(2) = 2 * 2 + 1

...

which is 5
```

Two slides headed "Evaluating", the second revealed in two presses.

```
## Lookups

games = [...]

<<<

games[0]

...

{"away_team": ...}

<<<

games[0]["away_team"]
```

Two slides, both topped by `games = [...]`: the first steps through `games[0]`
and its answer, the second replaces them with `games[0]["away_team"]`.

A `...` in a left column holds back the rest of it and the whole right column;
in the right column, just what follows it. `<<<` never reaches back past a `---`
or `##`. Tall slides scroll.

## Controls

Transitions are instant. Reveal's keys work (space, `o` overview, `s` notes, `f`
fullscreen, `?` help); `ctrl`+`←`/`→` jump between `##` sections; `alt`+`←`/`→`
are left to browser history. Append `&print-pdf` for a printable layout.

## Caching

Edits show up on the next load:

- Readmes are fetched with `cache: "no-cache"`, overriding
  `raw.githubusercontent.com`'s `max-age=300`.
- GitHub's CDN serves branch URLs up to five minutes stale, so content is read
  from the head commit's SHA instead. Reloading re-resolves it; navigating
  between decks reuses it.

The repo listing uses GitHub's tree API (60 requests/hour per IP, shared across
the school), so it's cached in `localStorage` for ten minutes and shown stale if
the limit is hit. Reloading always refetches. Decks fall back to the branch URL
if the listing is unavailable.

The site itself is served with `max-age=600`; hard-reload (ctrl+shift+R) to pick
up viewer changes immediately.

## Layout

```
index.html            contents
view.html             one deck
app/github.js         source parsing, fetching, link rewriting, listing
app/index.js          contents page
app/view.js           deck page
app/site.css          contents styling
app/slides.css        deck styling
app/google-light.css  highlight.js theme
vendor/reveal/        vendored reveal.js subset
scripts/              vendoring and tests
```

The class repo is the `CLASS_REPO` constant in `app/github.js`. It currently
points at the `solutions` branch, which is what anyone with the link sees.

## Development

Run from the repo root:

```sh
npm run serve    # http://localhost:6700 (Cache-Control: no-store)
npm test
npm run fmt
```

`file://` won't load ES modules, and `python -m http.server` lets the browser
cache `app/*.js`, so use `npm run serve`.

To update reveal.js, bump it in `package.json`, then
`npm install && npm run vendor`. `vendor/` is committed; only MathJax loads from
a CDN, and only on decks with math.
