import csv

# Read game data

with open("games.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers

for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])

eagles = "Philadelphia Eagles"

wins = 0
losses = 0
ties = 0

# Calculate wins and losses for the eagles

for game in games:
    if game["home_team"] == eagles:
        if game["home_score"] > game["away_score"]:
            wins += 1
        elif game["home_score"] < game["away_score"]:
            losses += 1
        else:
            ties += 1

    if game["away_team"] == eagles:
        if game["away_score"] > game["home_score"]:
            wins += 1
        elif game["away_score"] < game["home_score"]:
            losses += 1
        else:
            tie += 1

print("Eagles record:", wins, losses, ties)
