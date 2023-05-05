from models.menu import Menu
from views.menuView import MenuView


class MenuController:

    def __init__(self, menu_name, atts={}):
        self.menu = Menu(menu_name, atts)
        self.menuView = MenuView(self.menu)
        self.response = ''

    """ Verifier si la réponse est valide :
    La réponse doit être un nombre dans la liste proposée """
    def validate_response(self):
        if 0 < self.response <= len(self.menu.entries):
            return True
        else:
            return False
    """ Recevoir et traiter la réponse de l'utilisateur
    Prompt propose le menu contenu dans self.menu """
    def ask_user(self):
        self.response = self.menuView.prompt()
        if self.response.isdigit():
            self.response = int(self.response)
        else:
            self.menuView.user_error()
            return self.ask_user()

        while not self.validate_response():
            self.menuView.user_error()
            return self.ask_user()
        return self.response
