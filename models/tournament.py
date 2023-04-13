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
            rounds,
            players,
            notes,
            rounds
    """
    def __init__(self, atts):
        self.name = atts['name']
        self.location = atts['location']
        self.startDate = atts['startDate']
        self.endDate = atts['endDate']
        self.numberOfRounds = atts['numberOfRounds']
        self.currentRound = atts['currentRound']
        self.rounds = atts['rounds']
        if 'players' in atts:
            self.players = atts['players']
        else:
            self.players = []
        if 'players_ids' in atts:
            self.players_ids = atts['players_ids']
        else:
            self.players_ids = []
        self.players_ids = atts['players_ids'] if atts['players_ids'] else []
        self.notes = atts['notes']
        self.rounds = []

    """Ajout de joueurs à la liste des inscrits"""
    def add_player(self, player):
        self.players.append(player)

    def json_serialize(self):
        players = []
        if len(self.players) > 0:
            for player in self.players:
                players.append(player.idne)

        self.atts = {
            'name' : self.name,
            'location' : self.location,
            'startDate' : self.startDate,
            'endDate' : self.endDate,
            'numberOfRounds' : self.numberOfRounds,
            'currentRound' : self.currentRound,
            'rounds' : self.rounds,
            'players_ids' : players,
            'notes' : self.notes,
            'rounds' : self.rounds
        }
    
    def json_unserialize(self, json_datas):
        self.name = json_datas['name'],
        self.location = json_datas['location'],
        self.startDate = json_datas['startDate'],
        self.endDate = json_datas['endDate'],
        self.numberOfRounds = json_datas['numberOfRounds'],
        self.currentRound = json_datas['currentRound'],
        self.rounds = json_datas['rounds'],
        self.players_ids = json_datas['players_id'],
        self.notes = json_datas['notes'],
        self.rounds = json_datas['rounds']

    def __str__(self):
        return self.name