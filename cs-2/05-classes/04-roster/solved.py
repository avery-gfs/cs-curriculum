class Player:
    def __init__(self, name):
        self.name = name
        self.baskets = 0
        self.shots = 0

    def __repr__(self):
        return f"{self.name} {self.baskets}/{self.shots}"


class Team:
    def __init__(self):
        self.players = []

    def addPlayer(self, name):
        self.players.append(Player(name))

    def addBasket(self, name):
        for player in self.players:
            if player.name == name:
                player.baskets += 1
                player.shots += 1

    def addMiss(self, name):
        for player in self.players:
            if player.name == name:
                player.shots += 1

    def removePlayer(self, name):
        self.players = [p if p.name != name for p in players]

    def __repr__(self):
        numPlayers = len(self.players)
        totalBaskets = 0
        totalShots = 0
        playerRows = ""

        for player in self.players:
            playerRows += f"\n{player}"
            totalBaskets += player.baskets
            totalShots += player.shots

        return f"{numPlayers} players, {totalBaskets}/{totalShots} total{playerRows}"


print("Test player:\n")

avery = Player("Avery")
print(avery.name)  # "Avery"

avery.baskets = 2
avery.shots = 3
print(avery)  # Avery 2/3

print("\nTest roster:\n")

team = Team()

team.addPlayer("Judy")
team.addPlayer("Marcus")
team.addPlayer("Mercedes")

team.addBasket("Marcus")
team.addBasket("Marcus")

team.addMiss("Marcus")
team.addMiss("Judy")
team.addMiss("Mercedes")

team.removePlayer("Mercedes")

print(team)
