import csv

# Read game data

with open("games.csv") as file:
    games = list(csv.DictReader(file))

# Convert scores from strings to numbers

for game in games:
    game["away_score"] = int(game["away_score"])
    game["home_score"] = int(game["home_score"])


class TeamStats:
    # Each team will have its own TeamStats object

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.pointsScored = 0
        self.pointsAllowed = 0
        self.numGames = 0

    def addStatsHome(self, game):
        # Update team stats (numGames, wins, losses, ties, pointsScored,
        # and pointsAllowed) based on game info, knowing that this team
        # was the home team

        pass  # Your code goes here

    def addStatsAway(self, game):
        # Update team stats (numGames, wins, losses, ties, pointsScored,
        # and pointsAllowed) based on game info, knowing that this team
        # was the away team

        pass  # Your code goes here

    def winPercent(self):
        # Calculate the win percentage

        return 0  # Your code goes here

    def pointsScoredPerGame(self):
        # Calculate points scored per game

        return 0  # Your code goes here

    def pointsAllowedPerGame(self):
        # Calculate points allowed per game

        return 0  # Your code goes here

    def __repr__(self):
        result = ""

        result += f"name:                    {self.name}\n"
        result += f"number of games:         {self.numGames}\n"
        result += f"wins:                    {self.wins}\n"
        result += f"losses:                  {self.losses}\n"
        result += f"ties:                    {self.ties}\n"
        result += f"win percent:             {self.winPercent():.3f}\n"
        result += f"points scored:           {self.pointsScored}\n"
        result += f"points allowed:          {self.pointsAllowed}\n"
        result += f"points scored per game:  {self.pointsScoredPerGame():.1f}\n"
        result += f"points allowed per game: {self.pointsAllowedPerGame():.1f}\n"

        return result


# Keys are team names, values are TeamStats objects

stats = {}

# Update stats for home and away teams for each game

for game in games:
    homeTeam = game["home_team"]
    awayTeam = game["away_team"]

    stats.setdefault(homeTeam, TeamStats(homeTeam))
    stats.setdefault(awayTeam, TeamStats(awayTeam))

    stats[homeTeam].addStatsHome(game)
    stats[awayTeam].addStatsAway(game)

# Print final stats for each team

for team in stats:
    print(stats[team])

# Generate output CSV file for team stats
# The CSV table should start with the following header row

resultCSV = "name,wins,losses,ties,win_percent,points_scored,points_allowed,num_games,points_scored_per_game,points_allowed_per_game"

for team in stats:
    teamStats = stats[team]
    resultCSV += f"\n"

# Write output CSV

with open("stats.csv", "w") as file:
    file.write(resultCSV)
