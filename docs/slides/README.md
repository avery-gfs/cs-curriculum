# Slides

A static site that renders the readmes in
[avery-gfs/classes-26](https://github.com/avery-gfs/classes-26) as reveal.js
slide decks. Everything happens in the browser: the page fetches markdown and
images straight from GitHub, so there is no server to run and no build step
between editing a readme and presenting it.

Published at <https://avery-gfs.github.io/slides/>.

## Using it

- **`index.html`** — _Avery's CS Curriculum_ — lists every `readme.md` in the
  class repo by folder path, plus any top-level `.md` file, each linking to its
  rendered slides. `docs/` is left out as this site's own source.
- **`view.html?src=…`** renders one document. `src` is either a path inside the
  class repo (`cs-1/00-introduction`) or a link to any file or folder on GitHub:

  ```
  view.html?src=cs-1/00-introduction
  view.html?src=https://github.com/owner/repo/blob/main/README.md
  view.html?src=https://github.com/owner/repo/tree/main/docs
  ```

  A folder resolves to the `readme.md` inside it.

HTML comments are stripped, and relative links are rewritten: images to
`raw.githubusercontent.com`, other markdown to this viewer, everything else to
the file's page on GitHub.

A fenced code block only gets syntax highlighting when the fence names a
language. Bare ``` blocks are program output, not code, so they render verbatim
rather than being guessed at.

Slides split at every `##` heading. Within one, `---` and `...` on a line of
their own are both a step you advance to, and neither is ever drawn.

`---` **starts a fresh slide** carrying the same `##` heading, so what was on
screen is replaced. Use it to step through versions of one thing — an equation,
a diagram, a snippet — each landing where the last one was. `...` instead
**adds** the block after it below what's already shown, as a reveal fragment;
earlier blocks stay until the next `---`.

```
## Evaluating

f(2)

---

f(2) = 2 * 2 + 1

...

which is 5

---

Done
```

That is four slides: three headed "Evaluating" — the third arriving in two
presses — and whatever follows the next `##`. Blocks between two markers appear
together as one step, and `#/h/v/f` links still reopen a deck mid-reveal.

A `---` needs a blank line above it. Without one, markdown reads it as
underlining the line before, and so does this — the same as `Heading\n---`. Both
markers are ignored inside fenced code blocks.

The document's `# heading` doesn't get a title slide of its own — it becomes a
small running header at the top of every slide, and stays put while a slide
scrolls. Anything else above or below it is kept as the first slide. A slide too
tall for the screen scrolls instead of running off the bottom.

Slide changes are instant: no slide transition, no background cross-fade, and no
fragment fade. Reveal's own keys still work — space to advance, `o` for the
slide overview, `s` for speaker notes, `f` for fullscreen, `?` for the rest.
`alt`+`←` and `alt`+`→` are deliberately left to the browser, so they still move
through history rather than through the deck. `ctrl`+`←` and `ctrl`+`→` jump to
the previous and next `##` section, skipping all of that section's `---` slides
and `...` fragments. Appending `&print-pdf` to a deck URL gives the printable
layout.

Edits to a readme show up on the next load. Two caches sit in the way, and both
have to be dealt with:

- The browser would reuse a readme for five minutes without asking, because
  `raw.githubusercontent.com` sends `Cache-Control: max-age=300`. Fetching with
  `cache: "no-cache"` revalidates every time, and costs about 130 bytes when
  nothing has changed.
- GitHub's CDN then serves a _branch_ URL from an edge snapshot up to five
  minutes old — watch the `source` `age` header climb towards 300 — and no
  request header or query string gets past it. So content is read from the head
  commit's SHA instead, resolved from the tree call the listing already makes. A
  new commit is a new URL, so there is nothing stale to serve. Reloading
  re-resolves the head commit; moving between decks reuses it.

## Layout

```
index.html          contents
view.html           one deck
app/github.js       source parsing, fetching, link rewriting, the deck listing
app/index.js        contents page
app/view.js         deck page
app/site.css        contents styling
app/slides.css      deck styling (the theme these classes have always used)
app/google-light.css  highlight.js theme
vendor/reveal/      the subset of reveal.js we ship
scripts/            vendoring and tests
```

The class repo it reads is the `CLASS_REPO` constant at the top of
`app/github.js` — owner, repo, and branch. Note it currently points at the
`solutions` branch, which is what anyone with the link will see.

## Development

The package manifest lives at the repo root, so run these from there rather than
from this directory:

```sh
npm run serve    # http://localhost:6700
npm test         # checks parsing, link rewriting and the deck listing
npm run fmt      # deno fmt + ruff, over the whole repo
```

ES modules don't load over `file://`, so opening `index.html` directly won't
work; use the server. It's a dependency-free static server whose one opinion is
`Cache-Control: no-store` — a plain `python -m http.server` sends no cache
headers at all, which lets the browser heuristically cache `app/*.js` and makes
your edits look like they did nothing.

To update reveal.js, bump it in the repo-root `package.json`, then:

```sh
npm install && npm run vendor
```

`vendor/` is committed so the site has no CDN dependency. MathJax is the one
exception — reveal's math plugin loads it from jsDelivr, and only on decks that
contain math.

## Rate limits

Listing the class repo uses GitHub's tree API, which allows 60 requests per hour
per IP address — and a school shares one address. Conditional requests don't
help: unauthenticated `304`s count against the limit too. So the listing is
cached in `localStorage` for ten minutes, and a stale cache is shown rather than
an error if the limit is reached. Reloading the page refetches it regardless —
localStorage survives even a hard reload, so a listing that ignored the reload
would be impossible to shift — while ordinary navigation back to the contents
still uses the cache. Reloading is the only way to force a refetch. Opening a
deck doesn't touch the API beyond that shared listing, so slides keep working
regardless — without it they fall back to the branch URL, which is what happened
before.

The site's own files are served by GitHub Pages with `max-age=600`, so after
pushing a change to the viewer itself, a browser that has been here before may
run the old copy for up to ten minutes. A hard reload (ctrl+shift+R) skips it.
