const rows = $$("tr")
  .filter((tr) => !tr.classList.contains("header"))
  .map((tr) =>
    [...tr.querySelectorAll("td")].map((td) => td.innerText).slice(1, 5).join(
      ",",
    )
  )
  .join("\n");

console.log(`away_team,away_score,home_team,home_score\n${rows}`);
