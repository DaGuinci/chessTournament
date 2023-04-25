from .menuController import MenuController
from .tournamentController import TournamentController
from .playerController import PlayerController


class MainController:
    def __init__(self):
        self.tournament_controller = TournamentController()
        self.main_menu = MenuController('main_menu')

    """Accueil de l'utilisateur, demander quoi faire"""
    def run(self):
        choice = self.main_menu.ask_user()
        match choice:
            case 1:
                # Créer ou jouer un tournoi
                self.tournament_controller.main_tournament()
            case 2:
                # menu joueurs
                player_menu = MenuController('player_menu')
                player_controller = PlayerController()
                player_menu_choice = player_menu.ask_user()
                if player_menu_choice == 1:
                    player_controller.display_players()
                elif player_menu_choice == 2:
                    player_controller.create_player()
                elif player_menu_choice == 3:
                    pass
            case 4:
                exit()
            case _:
                print('Nous n\'avons pas compris votre choix.')
                print('Veuillez réessayer.')
        self.run()
