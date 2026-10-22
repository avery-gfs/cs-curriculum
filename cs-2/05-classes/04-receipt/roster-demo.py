class Player:
    def __init__(self, name):
        self.name = name
        # Every player starts with no baskets and no shots
        self.baskets = 0
        self.shots = 0

    def percent(self):
        # Percent of shots that went in (use max to avoid division by zero)
        return self.baskets / max(1, self.shots) * 100

    def __repr__(self):
        # Example: Avery 3/4 (75.00)
        # ':.2f' in the format string displays number with 2 decimal places
        return f"{self.name} {self.baskets}/{self.shots} ({self.percent():.2f})"


class Team:
    def __init__(self):
        # List of Player objects (players on team)
        self.players = []

    def addPlayer(self, name):
        # Make a new Player object with the given name and add them to the team
        self.players.append(Player(name))

    def addBasket(self, name):
        # Find the player with a matching name, increase their basket and shot
        # counts by 1 each
        for player in self.players:
            if player.name == name:
                player.baskets += 1
                player.shots += 1

    def addMiss(self, name):
        # Find the player with a matching name, increase their shot count by 1
        for player in self.players:
            if player.name == name:
                player.shots += 1

    def removePlayer(self, name):
        # Build a new list with every player except the one being removed
        newPlayers = []

        for player in self.players:
            if player.name != name:
                newPlayers.append(player)

        self.players = newPlayers

    def percent(self):
        # Percent of shots that went in for all players on the team

        totalBaskets = 0
        totalShots = 0

        for player in self.players:
            totalBaskets += player.baskets
            totalShots += player.shots

        # (use max to avoid division by zero)
        return totalBaskets / max(1, totalShots) * 100

    def __repr__(self):
        # One line per player, then a divider and the team average percent
        playerRows = ""

        for player in self.players:
            playerRows += f"{player}\n"

        return f"{playerRows}----------\naverage: {self.percent():.2f}"


a = Player("Avery")

print(a.name)  # Avery
print(a.baskets)  # 0
print(a.shots)  # 0
print(a.percent())  # 0.0
print(a)  # Avery 0/0 (0.00)

a.baskets = 3
a.shots = 4

print(a.percent())  # 75.0
print(a)  # Avery 3/4 (75.00)

team = Team()

team.addPlayer("Luna")
team.addPlayer("Marty")
team.addPlayer("Mercedes")

team.addBasket("Luna")
team.addMiss("Luna")

team.addBasket("Marty")
team.addBasket("Marty")
team.addBasket("Marty")
team.addMiss("Marty")
team.addBasket("Marty")

team.addBasket("Mercedes")

print(team.average())  # 70.0

print()
print(team)
print()

# Luna 1/2 (50.00)
# Marty 4/5 (80.00)
# Mercedes 1/1 (100.00)
# ----------
# average: 75.00

team.removePlayer("Mercedes")
team.addMiss("Luna")
team.addMiss("Luna")
team.addPlayer("Judy")
team.addBasket("Judy")

print(team.average())  # 45.0

print()
print(team)

# Luna 1/4 (25.00)
# Marty 4/5 (80.00)
# Judy 1/1 (100.00)
# ----------
# average: 60.00
