from models.tournament import Tournament
from models.tournamentsList import TournamentsList
from models.player import Player
from views.view import View
from views.createTournamentView import CreateTournamentView
from views.homeMenu import HomeMenu
from views.tournamentSelectView import TournamentSelectMenu

class Controller:
    def __init__(self):
        self.view = View()
        self.tournamentsList = TournamentsList()
        self.justArrived = True

    def create_player(self):
        firstName = self.view.askUser("Prénom : ")
        lastName = self.view.askUser("Nom de famille : ")
        birthDate = self.view.askUser("Date de naissance : ")
        idne = self.view.askUser("Identifiant nation d'échec : ")

        #ici verifier si les données de l'utilisateur sont bonnes
        player = Player(firstName, lastName, birthDate, idne)
        self.add_player_to_tournament(player)
        print("Joueur créé")

    def create_tournament(self):
        view = CreateTournamentView
        self.atts = view.askUserForTournamentInfos(view)
        # Vérifier le numéro du tour en cours
        self.atts['roundsList'] = []
        self.atts['playersList'] = []
        tournament = Tournament(self.atts)
        self.tournamentsList.add_tournament(tournament)
        print('\nTournoi créé.')
        self.launch()

    def add_player_to_tournament(self, tournament, player):
        tournament.add_player(player)
        print("Joueur ajouté")

    def display_tournament_list(self):
        self.view.display_players_list(self.tournament.playersList)
    
    def modify_tournament_section(self):
        menu = TournamentSelectMenu(self.tournamentsList.list)
        choice = menu.display_menu()
        print('votre choix :', choice)
        if choice.isdigit():
            choice = int(choice)
            # print(choice - 1)
            # print(type(choice))
            # print(len(self.tournamentsList.list))
            tournament = self.tournamentsList.list[choice - 1]
            print(tournament)
        elif choice == 'r':
            self.launch()
        else:
            print('Houston, nous avons un petit souci')

    def launch(self):
        if self.justArrived:
            print('\nBonjour,\nQue souhaitez-vous faire ?\n')
        else:
            print('\nQue souhaitez-vous faire ?\n')
            self.justArrived = False
        menu = HomeMenu()
        choice = menu.display_menu()
        match choice:
            case '1':
                self.create_tournament()
            case '2':
                self.modify_tournament_section()
            case '3':
                self.create_player()
            case _:
                print('Nous n\'avons pas compris votre choix. Veuillez réessayer.')


