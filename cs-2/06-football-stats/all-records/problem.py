import csv

# Read game data

with open("games.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers

for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])

# Keys are team names, values are the win, loss, and tie counts for each team

wins = {}
losses = {}
ties = {}

# Update stats for home and away teams for each game

for game in games:
    homeTeam = game["home_team"]
    homeScore = game["home_score"]

    awayTeam = game["away_team"]
    awayScore = game["away_score"]

    # Your code goes here

# Print final stats for each team

for team in wins:
    # Add code to print the win percentage for each team, showing three decimal
    # places for each win percentage value

    winPct = 0  # Your code goes here

    print(team, wins[team], losses[team], ties[team], winPct)
