from .menuController import MenuController
from .tournamentController import TournamentController
from .playerController import PlayerController


class MainController:
    def __init__(self):
        self.justArrived = True
        self.tournament_controller = TournamentController()

    """Accueil de l'utilisateur, demander quoi faire"""
    def run(self):
        main_menu = MenuController('main_menu')
        choice = main_menu.ask_user()
        match choice:
            case 1:
                # Créer ou jouer un tournoi
                self.tournament_controller.main_tournament()
                self.run()
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
                self.run()
            case 3:
                player_controller = PlayerController()
                player_controller.display_players()
                self.run()
            case _:
                print('Nous n\'avons pas compris votre choix.')
                print('Veuillez réessayer.')
