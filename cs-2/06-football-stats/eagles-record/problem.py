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
    pass

print("Eagles record:", wins, losses, ties)
