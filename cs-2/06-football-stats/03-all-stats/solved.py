import csv

# Read game data

with open("games.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers

for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])


class TeamStats:
    # Each team gets its own TeamStats object

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.pointsScored = 0
        self.pointsAllowed = 0
        self.numGames = 0

    def addStats(self, scored, allowed):
        # Update team stats (numGames, wins, losses, ties, pointsScored,
        # and pointsAllowed) based on game info

        self.numGames += 1

        if scored > allowed:
            self.wins += 1
        elif scored < allowed:
            self.losses += 1
        else:
            self.ties += 1

        self.pointsScored += scored
        self.pointsAllowed += allowed

    def winPercent(self):
        # Calculate the win percentage

        return self.wins / max(self.numGames, 1)

    def pointsScoredPerGame(self):
        # Calculate points scored per game

        return self.pointsScored / max(self.numGames, 1)

    def pointsAllowedPerGame(self):
        # Calculate points allowed per game

        return self.pointsAllowed / max(self.numGames, 1)

    def csvRow(self):
        # Write a single CSV line representing the data for this team, with rounding as shown
        # Format: name,num_games,wins,losses,ties,win%,points_scored,points_allowed,points_scored/game,points_allowed/game
        # Example: Philadelphia Eagles,17,11,6,0,0.647,379,325,17,22.3,19.1

        return f"{self.name},{self.numGames},{self.wins},{self.losses},{self.ties},{self.winPercent():.3f},{self.pointsScored},{self.pointsAllowed},{self.pointsScoredPerGame():.1f},{self.pointsAllowedPerGame():.1f}"

    def __repr__(self):
        return "\n".join([
            f"name:                    {self.name}",
            f"number of games:         {self.numGames}",
            f"wins:                    {self.wins}",
            f"losses:                  {self.losses}",
            f"ties:                    {self.ties}",
            f"win percent:             {self.winPercent():.3f}",
            f"points scored:           {self.pointsScored}",
            f"points allowed:          {self.pointsAllowed}",
            f"points scored per game:  {self.pointsScoredPerGame():.1f}",
            f"points allowed per game: {self.pointsAllowedPerGame():.1f}",
        ])


# Keys are team names, values are TeamStats objects

stats = {}

# Update stats for home and away teams for each game

for game in games:
    homeTeam = game["home_team"]
    awayTeam = game["away_team"]

    stats.setdefault(homeTeam, TeamStats(homeTeam))
    stats.setdefault(awayTeam, TeamStats(awayTeam))

    stats[homeTeam].addStats(game["home_score"], game["away_score"])
    stats[awayTeam].addStats(game["away_score"], game["home_score"])

# Print final stats for each team

for team in stats:
    print(stats[team], "\n")

# Generate output CSV file for team stats
# The CSV table should start with the following header row

resultCSV = "name,num_games,wins,losses,ties,win_percent,points_scored,points_allowed,points_scored_per_game,points_allowed_per_game\n"

for team in stats:
    resultCSV += f"{stats[team].csvRow()}\n"

# Write output CSV

with open("stats.csv", "w") as file:
    file.write(resultCSV)
