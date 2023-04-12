class MenuView:

    """Initialize : menu is a liste"""
    def __init__(self, menu) -> None:
        self.menu = menu

    """Display the menu"""
    def prompt(self):
        print('\n')
        print('=============================')
        print(self.menu.title.upper())
        print('=============================')
        print(self.menu.intro)
        print('\n')
        for i, entry in enumerate(self.menu.entries):
            i += 1
            print(i, entry)
        print('\n')
        return input('Quel est votre choix ?\n')
    
    def user_error(self):
        print('Désolé, votre réponse n\'est pas valide.\nVeuillez réessayer')