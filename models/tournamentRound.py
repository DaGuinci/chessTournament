"""Un round possède comme attributs :
un nom(str)
une liste de matchs
horodatage auto debut
horodatage auto fin
"""


class TournamentRound:

    def __init__(self, atts):
        self.tournament = atts['tournament']
        self.name = atts['name']
        self.games = atts['games']
        # TODO Gérer les remplissage auto des horodatages
        self.start = ''
        self.end = ''

    def json_serialize(self):
        self.atts = {
            'tournament': self.tournament,
            'name': self.name,
            'games': self.games,
            'start': self.start,
            'end': self.end
        }
