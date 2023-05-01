# from .menuController import MenuController
from .dataController import DataController
from models.player import Player
from views.playerView import PlayerView


class PlayerController:

    def __init__(self):
        self.players = []
        self.view = PlayerView()
        self.data_controller = DataController()
        self.init_players()

    """Chargement de la liste des joueurs existants"""
    def init_players(self):
        players = self.data_controller.load_players()
        for player in players:
            p = Player(player)
            self.players.append(p)

    """Création d'un nouveau joueur"""
    def create_player(self, tournament=False):
        """Obtenir les infos pour création d'un joueur"""
        atts = self.view.ask_user_for_new()

        #  Si le joueur existe, refuser la création
        for player in self.players:
            if player.idne == atts['idne']:
                print('Cet identifant existe deja')
                return False

        """Création du joueur"""
        player = Player(atts)
        self.players.append(player)
        self.data_controller.save_players(self.players)
        if tournament:
            tournament.add_player(player)
        print('\nJoueur créé.')

    def get_player_by_id(self, id):
        for player in self.players:
            if player.idne == id:
                return player

    def get_player_name_by_id(self, id):
        for player in self.players:
            if player.idne == id:
                return f'{player.firstName} {player.lastName}'

    """Affichage de la liste de joueurs"""
    def display_players(self):
        self.view.display_players(self.players)
