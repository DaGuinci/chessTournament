"""Classe tournoi : nom du tournoi, liste de joueurs inscrits"""

class Tournament:

    """Initialisation du tournoi
    atts est un dictionnaire comprenant :
            name,
            location,
            startDate,
            endDate,
            numberOfRounds = 4,
            currentRound,
            roundsList,
            playersList,
            notes
    """
    def __init__(self, atts):
        
        self.name = atts['name']
        self.location = atts['location']
        self.startDate = atts['startDate']
        self.endDate = atts['endDate']
        self.numberOfRounds = atts['numberOfRounds']
        self.currentRound = atts['currentRound']
        self.roundsList = atts['roundsList']
        self.playersList = atts['playersList']
        self.notes =atts['notes']


    """Ajout de joueurs à la liste des inscrits"""
    def add_player(self, player):
        self.playersList.append(player)

    def __str__(self):
        return self.name