from models.menu import Menu
from views.menuView import MenuView

class MenuController:

    def __init__(self, menu_name, atts = {}):
        self.menu = Menu(menu_name, atts)
        self.menuView = MenuView(self.menu)
        self.response = ''

    """Verify if the user response is valide :
    Response has to be a number in the menu list"""
    def validate_response(self):
        if self.response.isdigit():
            self.response = int(self.response)
            if 0 < self.response <= len(self.menu.entries):
                return True
            else:
                return False
        else:
            return False

    def ask_user(self):
        self.response = self.menuView.prompt()
        if self.validate_response():
            return self.response
        else:
            self.menuView.user_error()
            self.ask_user()
