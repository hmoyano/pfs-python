# Auth: Hector Moyano
# Version: 0.0.1
# data: 15/03/2022

class Team():

    # Atributos de clase
    players = []

    # Contructor de clase
    def __init__(self):
        pass

    # Metodos de clase
    def addPlayer(self, newPlayer):
        self.players.append(newPlayer)

    def getPlayers(self):
        print(self.players[0])
