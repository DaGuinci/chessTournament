class ModifyTournamentView:

    def __init__(self, tournament) -> None:
        self.tournament = tournament
        self.modifyMenu = [
            '1. Afficher les détails du tournoi',
            '2. Afficher la liste des joueurs inscrits',
            '3. Ajouter un joueur',
        ]
    
    def mainModifyTournamentMenu(self):
        for entry in self.modifyMenu:
            print(entry)
        return input('Votre choix :\n')

    def displayTournamentDetails(self):
        print('Nom du tournoi : ', self.tournament.name)
        print('Lieu du tournoi : ', self.tournament.location)