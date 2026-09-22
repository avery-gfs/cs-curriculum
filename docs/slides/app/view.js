import Reveal from "../vendor/reveal/dist/reveal.esm.js";
import RevealMarkdown from "../vendor/reveal/plugin/markdown/markdown.esm.js";
import RevealMath from "../vendor/reveal/plugin/math/math.esm.js";
import RevealHighlight from "../vendor/reveal/plugin/highlight/highlight.esm.js";
import RevealNotes from "../vendor/reveal/plugin/notes/notes.esm.js";

import {
  fetchMarkdown,
  labelledSlideIndexes,
  parseSource,
  pinToHead,
  prepareMarkdown,
  splitSlides,
  splitTitle,
} from "./github.js";

// `splitSlides` has already cut the document up, so each section below holds
// exactly one slide and reveal must not split it again. Left to itself it breaks
// at every `---` line, and a pattern that can't match is the only way off.
const NO_SEPARATOR = "(?!)";

// Reveal's own speaker view and console debugging both expect this global; the
// ES module build doesn't set it.
window.Reveal = Reveal;

const slidesEl = document.getElementById("slides");
const messageEl = document.getElementById("deck-message");
let labelledSlides = [];

keepBrowserHistoryKeys();
addSectionNavigation();

// Reveal reads the URL during initialize, before the fragments below exist, and
// rewrites it without the fragment index — so keep a copy of what was asked for.
const requestedHash = location.hash;

const src = new URLSearchParams(location.search).get("src");
if (src === null) location.replace("index.html");
else show(src);

async function show(src) {
  // Reading a deck from the head commit rather than the branch is what makes an
  // edit show up straight away. A reload re-resolves it, so the usual way of
  // asking for the current version does the right thing.
  await pinToHead({ force: isReload() });

  let loc, markdown;
  try {
    const found = await fetchMarkdown(parseSource(src));
    loc = found.loc;
    markdown = prepareMarkdown(found.text, loc);
  } catch (err) {
    fail(err.message);
    return;
  }

  const { title, body } = splitTitle(markdown);

  document.title = title || loc.path || "Slides";

  const slides = splitSlides(body);
  labelledSlides = labelledSlideIndexes(body);
  for (const slide of slides.length ? slides : [body]) {
    slidesEl.append(deckSection(slide));
  }

  await Reveal.initialize({
    hash: true,
    history: false,
    center: false,
    controls: false,
    progress: false,
    transition: "none",
    // Reveal normally lays a deck out in a fixed 960x700 coordinate space and
    // scales it to fill the window, which makes browser zoom do nothing: the
    // window shrinks, the scale factor grows to match, and the text stays put.
    // Sizing the deck at 100% of the window instead pins the scale at 1, so a
    // CSS pixel is a real pixel and zooming out makes text smaller and fits
    // more on screen, the way it does on any other page.
    width: "100%",
    height: "100%",
    margin: 0,
    minScale: 1,
    maxScale: 1,
    // Reveal still cross-fades the slide *background* over 0.8s even when the
    // slide transition is off.
    backgroundTransition: "none",
    highlight: {
      // Runs once reveal has parsed the markdown and gathered the code blocks,
      // but before any of them have been highlighted.
      beforeHighlight: markPlainCodeBlocks,
    },
    plugins: [RevealMarkdown, RevealMath, RevealHighlight, RevealNotes],
  });

  addFragments();
  if (title) addRunningHeader(title);

  // Both of the above rewrite slides reveal has already parsed.
  Reveal.sync();
  applyRequestedFragment();
  Reveal.layout();
}

// A fence with no language is program output or pseudocode, not code in some
// language, but highlight.js guesses one anyway — the "Hello world!" output of a
// python example comes out coloured as AppleScript. Declaring those blocks
// plaintext makes hljs render them verbatim while still styling them as code.
function markPlainCodeBlocks(hljs) {
  for (const code of slidesEl.querySelectorAll("pre code")) {
    // Mirrors how hljs resolves a block's language: a `language-x` or `lang-x`
    // class, or any class that happens to name a language it knows (a bare
    // ```py fence becomes class="py").
    const classes = `${code.className} ${code.parentNode.className}`;
    const declared = /\blang(?:uage)?-[\w-]+\b/i.test(classes) ||
      classes.split(/\s+/).some((name) => name && hljs.getLanguage(name));

    if (!declared) code.classList.add("language-plaintext");
  }
}

// A `...` between blocks marks a fragment break: everything after it waits for
// the next press. Reveal groups fragments that share an index, so each run of
// content between markers appears as one step, and the markers themselves go
// away. (`---` is not handled here — it became a slide of its own upstream.)
function addFragments() {
  for (const slide of slidesEl.querySelectorAll("section[data-markdown]")) {
    let index = 0;
    for (const node of [...slide.children]) {
      if (isFragmentBreak(node)) {
        node.remove();
        index += 1;
      } else if (index) {
        node.classList.add("fragment");
        node.dataset.fragmentIndex = index;
      }
    }
  }
}

// A paragraph that is nothing but `...` (or `…`, if something smartened it).
function isFragmentBreak(node) {
  return (
    node.tagName === "P" &&
    !node.firstElementChild &&
    /^(\.\.\.|…)$/.test(node.textContent.trim())
  );
}

function isReload() {
  try {
    return performance.getEntriesByType("navigation")[0]?.type === "reload";
  } catch {
    return false;
  }
}

// Sets how much of the opening slide is revealed. Reveal reached that slide
// before it had any fragments, so syncing them in leaves every one of them
// showing — landing there from a link or a reload would give the answer away.
// The hash is `#/h/v/f`; these slides carry no ids, so a third component is
// always a fragment index, and -1 means nothing revealed yet.
function applyRequestedFragment() {
  const parts = requestedHash.replace(/^#\/?/, "").split("/");
  const asked = parts.length === 3 ? Number(parts[2]) : NaN;

  const { h, v } = Reveal.getIndices();
  Reveal.slide(h, v, Number.isInteger(asked) ? asked : -1);
}

// The markdown goes in as text, never as HTML, so a document can't inject
// markup into this page just by being rendered.
function deckSection(markdown) {
  const section = document.createElement("section");
  section.setAttribute("data-markdown", "");
  section.setAttribute("data-separator", NO_SEPARATOR);

  const template = document.createElement("textarea");
  template.setAttribute("data-template", "");
  template.textContent = markdown;

  section.append(template);
  return section;
}

// Reveal has already turned the markdown into slides by now, so the header goes
// in as a real element — one per slide, sticky so it stays put while a long
// slide scrolls underneath it.
function addRunningHeader(title) {
  for (const slide of slidesEl.querySelectorAll("section[data-markdown]")) {
    const header = document.createElement("div");
    header.className = "deck-header";
    header.textContent = title;
    slide.prepend(header);
  }
}

// Reveal reads alt+arrow as "advance past fragments" and swallows the event,
// which would take alt+left/right away from anyone using them to move through
// browser history. Stopping the event before reveal's own document listener
// leaves the browser's default navigation intact.
function keepBrowserHistoryKeys() {
  document.addEventListener(
    "keydown",
    (event) => {
      if (event.altKey && ["ArrowLeft", "ArrowRight"].includes(event.key)) {
        event.stopImmediatePropagation();
      }
    },
    true,
  );
}

// Ctrl+arrow moves between the `##` sections in the source. A section can span
// several slides (`---`) and fragment steps (`...`), so use the source-derived
// starts instead of Reveal's next/previous navigation.
function addSectionNavigation() {
  document.addEventListener(
    "keydown",
    (event) => {
      if (!event.ctrlKey || !["ArrowLeft", "ArrowRight"].includes(event.key)) {
        return;
      }

      const { h } = Reveal.getIndices();
      const current = labelledSlides.findLast((index) => index <= h);
      const target = event.key === "ArrowRight"
        ? labelledSlides.find((index) => index > (current ?? -1))
        : labelledSlides.findLast((index) => index < (current ?? Infinity));

      if (target === undefined) return;

      event.preventDefault();
      event.stopImmediatePropagation();
      Reveal.slide(target, 0, -1);
    },
    true,
  );
}

function fail(message) {
  document.title = "Slides — not found";
  document.querySelector(".reveal").hidden = true;

  const heading = document.createElement("h1");
  heading.textContent = "Couldn't open that";

  const detail = document.createElement("p");
  detail.textContent = message;

  const asked = document.createElement("p");
  asked.className = "asked";
  asked.textContent = src;

  const back = document.createElement("a");
  back.href = "index.html";
  back.textContent = "Back to the contents";

  messageEl.append(heading, detail, asked, back);
  messageEl.hidden = false;
}
