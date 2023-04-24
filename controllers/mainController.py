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
        #  if self.justArrived:
        #      print('\nBonjour,\nQue souhaitez-vous faire ?\n')
        #      self.justArrived = False
        #  else:
        #      print('\nQue souhaitez-vous faire ?\n')
        #  menu = HomeMenu()
        match choice:
            case 1:
                """Créer / jouer un tournoi"""
                self.tournament_controller.main_tournament()
                self.run()
            case 2:
                """Enregistrer un nouveau joueur"""
                player_controller = PlayerController()
                player_controller.create_player()
                self.run()
            case 3:
                """Afficher la liste des joueurs"""
                player_controller = PlayerController()
                player_controller.display_players()
                self.run()
            case _:
                print('Nous n\'avons pas compris votre choix.')
                print('Veuillez réessayer.')
