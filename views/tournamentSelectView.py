class TournamentSelectMenu:

    def __init__(self, list) -> None:
        self.entries = list
    
    def display_menu(self):
        print('Liste des tournois créés :\n')
        for i, entry in enumerate(self.entries):
            print(i+1, entry.name)
        msg = 'Quel tournoi souhaitez-vous modifier ?'
        msg += '(entrez \'r\' pour revenir au menu principal)\n'
        return input(msg)