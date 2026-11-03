# Sports Stats

## Data Scraping

https://www.footballdb.com/games/index.html

```js
const rows = $$("tr")
  .filter((tr) => !tr.classList.contains("header"))
  .map((tr) =>
    [...tr.querySelectorAll("td")].map((td) => td.innerText).slice(1, 5).join(
      ",",
    )
  )
  .join("\n");

console.log(`away_team,away_score,home_team,home_score\n${rows}`);
```

## CSV Files

CSV: "Comma separated values".

"Tabular data" (data in a table). Like a spreadsheet.

...

```txt
away_team,away_score,home_team,home_score
Dallas Cowboys,20,Philadelphia Eagles,24
Kansas City Chiefs,21,Los Angeles Chargers,27
Arizona Cardinals,20,New Orleans Saints,13
Pittsburgh Steelers,34,New York Jets,32
Miami Dolphins,8,Indianapolis Colts,33
...
```

...

- Header row
- Records
- Can import and export with spreadsheet programs

## Loading CSVs

```txt
away_team,away_score,home_team,home_score
Dallas Cowboys,20,Philadelphia Eagles,24
Kansas City Chiefs,21,Los Angeles Chargers,27
Arizona Cardinals,20,New Orleans Saints,13
Pittsburgh Steelers,34,New York Jets,32
Miami Dolphins,8,Indianapolis Colts,33
...
```

...

```py
import csv

# Read game data
with open("games.csv") as file:
    games = list(csv.DictReader(file))
```

...

```py
[
    {
        "away_team": "Dallas Cowboys",
        "away_score": "20",
        "home_team": "Philadelphia Eagles",
        "home_score": "24",
    },
    {
        "away_team": "Kansas City Chiefs",
        "away_score": "21",
        "home_team": "Los Angeles Chargers",
        "home_score": "27",
    },
    {
        "away_team": "Arizona Cardinals",
        "away_score": "20",
        "home_team": "New Orleans Saints",
        "home_score": "13",
    },
    {
        "away_team": "Pittsburgh Steelers",
        "away_score": "34",
        "home_team": "New York Jets",
        "home_score": "32",
    },
    {
        "away_team": "Miami Dolphins",
        "away_score": "8",
        "home_team": "Indianapolis Colts",
        "home_score": "33",
    },
    # ...
]
```

## Converting Numbers

```txt
away_team,away_score,home_team,home_score
Dallas Cowboys,20,Philadelphia Eagles,24
Kansas City Chiefs,21,Los Angeles Chargers,27
Arizona Cardinals,20,New Orleans Saints,13
Pittsburgh Steelers,34,New York Jets,32
Miami Dolphins,8,Indianapolis Colts,33
...
```

```py
import csv

# Read game data
with open("games.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers
for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])
```

<div style="font-size: 16px;">

```py
[
    {
        "away_team": "Dallas Cowboys",
        "away_score": 20,
        "home_team": "Philadelphia Eagles",
        "home_score": 24,
    },
    {
        "away_team": "Kansas City Chiefs",
        "away_score": 21,
        "home_team": "Los Angeles Chargers",
        "home_score": 27,
    },
    {
        "away_team": "Arizona Cardinals",
        "away_score": 20,
        "home_team": "New Orleans Saints",
        "home_score": 13,
    },
    {
        "away_team": "Pittsburgh Steelers",
        "away_score": 34,
        "home_team": "New York Jets",
        "home_score": 32,
    },
    {
        "away_team": "Miami Dolphins",
        "away_score": 8,
        "home_team": "Indianapolis Colts",
        "home_score": 33,
    },
    # ...
]
```

</div>

## Review Dictionaries
