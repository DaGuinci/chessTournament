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
        self.notes = atts['notes']


    """Ajout de joueurs à la liste des inscrits"""
    def add_player(self, player):
        self.playersList.append(player)

    def json_serialize(self):
        self.atts = {
            'name' : self.name,
            'location' : self.location,
            'startDate' : self.startDate,
            'endDate' : self.endDate,
            'numberOfRounds' : self.numberOfRounds,
            'currentRound' : self.currentRound,
            'roundsList' : self.roundsList,
            'playersList' : self.playersList,
            'notes' : self.notes
        }
    
    def json_unserialize(self, json_datas):
        self.name = json_datas['name'],
        self.location = json_datas['location'],
        self.startDate = json_datas['startDate'],
        self.endDate = json_datas['endDate'],
        self.numberOfRounds = json_datas['numberOfRounds'],
        self.currentRound = json_datas['currentRound'],
        self.roundsList = json_datas['roundsList'],
        self.playersList = json_datas['playersList'],
        self.notes = json_datas['notes']

    def __str__(self):
        return self.name