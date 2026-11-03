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

    wins.setdefault(homeTeam, 0)
    wins.setdefault(awayTeam, 0)

    losses.setdefault(homeTeam, 0)
    losses.setdefault(awayTeam, 0)

    ties.setdefault(homeTeam, 0)
    ties.setdefault(awayTeam, 0)

    if game["home_score"] > game["away_score"]:
        wins[homeTeam] += 1
        losses[awayTeam] += 1
    elif game["home_score"] < game["away_score"]:
        losses[homeTeam] += 1
        wins[awayTeam] += 1
    else:
        ties[homeTeam] += 1
        ties[awayTeam] += 1

# Print final stats for each team

for team in wins:
    # Add code to print the win percentage for each team, showing three decimal
    # places for each win percentage value

    total = wins[team] + losses[team] + ties[team]
    winPct = (wins[team] + 0.5 * ties[team]) / total

    print(team, wins[team], losses[team], ties[team], f"{winPct:.3f}")
