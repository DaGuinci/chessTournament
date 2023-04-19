# from models.tournament import Tournament
# from models.player import Player
# from views.view import View
# from views.createTournamentView import CreateTournamentView
# from views.homeMenu import HomeMenu
# from views.tournamentSelectView import TournamentSelectMenu
# from views.modifyTournamentView import ModifyTournamentView
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
        # if self.justArrived:
        #     print('\nBonjour,\nQue souhaitez-vous faire ?\n')
        #     self.justArrived = False
        # else:
        #     print('\nQue souhaitez-vous faire ?\n')
        # menu = HomeMenu()
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
                print('Nous n\'avons pas compris votre choix. Veuillez réessayer.')









    # def create_player(self):
    #     firstName = self.view.askUser("Prénom : ")
    #     lastName = self.view.askUser("Nom de famille : ")
    #     birthDate = self.view.askUser("Date de naissance : ")
    #     idne = self.view.askUser("Identifiant nation d'échec : ")

    #     #ici verifier si les données de l'utilisateur sont bonnes
    #     player = Player(firstName, lastName, birthDate, idne)
    #     self.add_player_to_tournament(player)
    #     print("Joueur créé")

    # def add_player_to_tournament(self, tournament, player):
    #     tournament.add_player(player)
    #     print("Joueur ajouté")

    # def display_tournament_list(self):
    #     self.view.display_players_list(self.tournament.playersList)

    # def modifyTournament(self, tournament):
    #     prompt = ModifyTournamentView(tournament)
    #     choice = prompt.mainModifyTournamentMenu() 
    #     match choice:
    #         case '1':
    #             prompt.displayTournamentDetails()       
    
    # def modify_tournament_section(self):
    #     menu = TournamentSelectMenu(self.tournamentsList)
    #     choice = menu.display_menu()
    #     print('votre choix :', choice)
    #     if choice.isdigit():
    #         choice = int(choice) - 1
    #         if 0 <= choice < len(self.tournamentsList):
    #             tournament = self.tournamentsList[choice]
    #             self.modifyTournament(tournament)
    #         else:
    #             print('Votre choix n\'est pas dans la liste !\nRéessayez, svp\n')
    #             self.modify_tournament_section()
    #     elif choice == 'r':
    #         self.run()
    #     else:
    #         print('Houston, nous avons un petit souci')
