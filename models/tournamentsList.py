class TournamentsList:
    def __init__(self):
        self.list = []
    
    def add_tournament(self, tournament):
        self.list.append(tournament)

    def __str__(self):
        result = 'Liste des tournois créés :\n'
        for tournament in self.list:
           result += tournament.name

        return result
    
    def __repr__(self):
        return str(self)