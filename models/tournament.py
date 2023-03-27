"""Classe tournoi : nom du tournoi, liste de joueurs inscrits"""

class Tournament:

    """Initialisation du tournoi"""
    def __init__(self, name):
        self.name = name
        self.players = []

    """Ajout de joueurs à la liste des inscrits"""
    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return self.name