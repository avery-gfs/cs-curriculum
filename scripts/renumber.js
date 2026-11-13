// Renumbers NN-name entries (files and dirs) so numbers are contiguous
// starting at 01. Ties (duplicate numbers) are ordered by name.
// Applies to the whole project (every directory under the repo root).
// A single letter after the number (03a-foo, 03b-bar) orders entries that share
// a number; letters are dropped when renumbering. No letter sorts first.
// Numbering starts at 00 if a directory already has a 00- entry, else 01.
// Usage: npm run renumber [-- -y]   (-y skips the confirmation prompt)
import fs from "node:fs";
import path from "node:path";
import readline from "node:readline/promises";

const yes = process.argv.includes("-y");
const skip = new Set(["node_modules", ".git", "vendor"]);

const root = path.resolve(import.meta.dirname, "..");

function plan(dir) {
  const entries = fs
    .readdirSync(dir)
    .map((name) => ({ name, m: name.match(/^(\d+)([a-z])?-(.*)$/) }))
    .filter((e) => e.m)
    .map((e) => ({
      name: e.name,
      num: Number(e.m[1]),
      letter: e.m[2] ?? "",
      rest: e.m[3],
    }))
    .sort(
      (a, b) =>
        a.num - b.num ||
        a.letter.localeCompare(b.letter) ||
        a.name.localeCompare(b.name),
    );
  const first = entries[0]?.num === 0 ? 0 : 1;
  const width = Math.max(2, String(entries.length + first).length);
  return entries
    .map((e, i) => ({
      from: e.name,
      to: `${String(i + first).padStart(width, "0")}-${e.rest}`,
    }))
    .filter((r) => r.from !== r.to);
}

async function confirm() {
  if (yes) return true;
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
  const answer = await rl.question("Apply? [y/N] ");
  rl.close();
  return /^y(es)?$/i.test(answer.trim());
}

async function run(dir) {
  // Children first, so renaming this level doesn't invalidate their paths.
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.isDirectory() && !skip.has(e.name)) {
      await run(path.join(dir, e.name));
    }
  }

  const renames = plan(dir);
  if (renames.length === 0) return;

  console.log(`${path.relative(root, dir) || "."}:`);
  for (const r of renames) console.log(`  ${r.from} -> ${r.to}`);
  if (!(await confirm())) {
    console.log("Aborted.");
    process.exit(1);
  }

  // Two phases via temp names so still-occupied targets don't collide.
  const tmp = (i) => `.renumber-tmp-${i}`;
  renames.forEach((r, i) =>
    fs.renameSync(path.join(dir, r.from), path.join(dir, tmp(i)))
  );
  renames.forEach((r, i) =>
    fs.renameSync(path.join(dir, tmp(i)), path.join(dir, r.to))
  );
}

await run(root);
