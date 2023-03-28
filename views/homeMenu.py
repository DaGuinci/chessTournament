class HomeMenu:

    def __init__(self) -> None:
        self.entries = [
            '1. Créer un tournoi',
            '2. Modifier un tournoi existant',
            '3. Créer un joueur'
        ]
    
    def display_menu(self):

        for entry in self.entries:
            print(entry)

        response = input('Quel est votre choix ?\n')
        return response