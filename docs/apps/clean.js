import { readFile, writeFile } from "fs/promises";

const file = process.argv[2];
const text = await readFile(file, "utf8");

const result = text
  .toLowerCase()
  .replace(/\[\d+\]/g, "")
  .replace(/[\[\]():;?!*_"“”,\r\n‘—]/g, " ")
  .replace(/[^\w]\.|\.[^\w]/g, " . ")
  .replace(/’ /g, " ")
  .replace(/’/g, "'")
  .replace(/\s+/g, "\n");

await writeFile(file, result);
