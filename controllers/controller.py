from models.tournament import Tournament
from models.player import Player
from views.view import View

class Controller:
    def __init__(self):
        self.view = View()
        pass

    def create_player(self, lastName = "Doe", birthDate = "01/01/2001", idne = "123456"):
        firstName = self.view.askUser("Prénom : ")
        player = Player(firstName, lastName, birthDate, idne)
        self.add_player_to_tournament(player)
        print("Joueur créé")

    def create_tournament(self, tournamentName):
        self.tournament = Tournament(tournamentName)
        print(self.tournament)

    def add_player_to_tournament(self, player):
        self.tournament.add_player(player)
        print("Joueur ajouté")

    def display_tournament_list(self):
        self.view.display_players_list(self.tournament.players)

    
