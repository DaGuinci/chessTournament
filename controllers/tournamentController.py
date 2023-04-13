"""Classe de controleur de tournois"""
from .menuController import MenuController
from .dataController import DataController
from controllers.playerController import PlayerController
from models.tournament import Tournament
from views.tournamentView import TournamentView

class TournamentController:
    def __init__(self):
        self.tournaments = []
        self.view = TournamentView()
        self.data_controller = DataController()
        self.player_controller = PlayerController()
        self.init_tournaments()

    """chargement initial des tournois à l'ouverture du programme"""
    def init_tournaments(self):
        tournaments = self.data_controller.load_tournaments()
        players = self.player_controller.players
        for tournament in tournaments:
            t = Tournament(tournament)
            for player_id in t.players_ids:
                for player in players:
                    if player_id == player.idne:
                        t.add_player(player)
            print(t.players)
            self.tournaments.append(t)

    """Sauvegarde de l'état"""
    def save(self):
        self.data_controller.save_tournaments(self.tournaments)

    """créer ou jouer un tournoi"""
    def main_tournament(self):
        menu = MenuController('main_tournament')
        choice = menu.ask_user()

        match choice:
            case 1:
                """Création d'un nouveau tournoi"""
                self.create_tournament()

            case 2:
                """Selection d'un tournoi existant"""
                if (len(self.tournaments) == 0):
                    print('Aucun tournoi n\'a encore été créé')
                    self.main_tournament()
                else:
                    self.select_tournament()
            
            case 3:
                """Retour au menu principal"""
                pass

    """Création d'un tournoi"""
    def create_tournament(self):
        """Obtenir les infos pour création d'un tournoi"""
        atts = self.view.ask_user_for_new()
        # Vérifier le numéro du tour en cours
        atts['rounds'] = []
        atts['players'] = []
        atts['players_ids'] = []

        tournament = Tournament(atts)
        self.tournaments.append(tournament)
        self.save()
        print('\nTournoi créé.')

    """Sélection d'un tournoi"""
    def select_tournament(self):
        tournaments = []
        for t in self.tournaments:
            tournaments.append(t)
        atts = {
            'tournaments' : tournaments
        }
        menu = MenuController('select_tournament', atts)
        choice = menu.ask_user()
        self.modify_tournament(choice - 1)
        """TODO Dernier choix : revenir au menu principal"""
    
    # def display_tournament_players(self, tournament_id):
    #     players = self.tournaments[tournament_id].players
    #     self.view.display_players(players)

    def modify_tournament(self, tournament_id):
        tournament = self.tournaments[tournament_id]
        atts = {
            'tournament' : tournament
        }
        menu = MenuController('modify_tournament', atts)
        choice = menu.ask_user()
        match choice:
            case 1:
                self.subscribe_player(tournament)

    """Inscrire des joueurs"""
    def subscribe_player(self, tournament):
        """Menu joueur existant ou créer un joueur"""
        atts = {
            'tournament' : tournament
        }
        menu = MenuController('subscribe_player', atts)
        choice = menu.ask_user()
        match choice:
            case 1:
                """inscrire un joueur existant :
                Demander l'id du joueur"""
                player_id = self.view.ask_user_for_player_id()
                
                """Vérifier si le joueur existe"""
                players = self.player_controller.players
                player_exists = False
                for player in players:
                    if player_id == player.idne:
                        player_exists = True

                """TODO Vérfifier que le joueur n'est pas déjà inscrit"""
                player_yet_in_tournament = False
                for player_in_tournament in tournament.players:
                    if player_id == player_in_tournament.idne:
                        player_yet_in_tournament = True
                
                """Inscrire le joueur"""
                if player_exists and not player_yet_in_tournament:
                    tournament.add_player(player)
                    self.save()
                    self.view.display_tournament_players(tournament)

                if not player_exists:
                    """TODO générer des messages d'erreur"""
                    print('Désolé, ce joueur n\'existe pas, veuillez réessayer')
                    self.subscribe_player(tournament)
                
                if player_yet_in_tournament:
                    """TODO générer des messages d'erreur"""
                    print('Ce joueur est déjà inscrit. Veuillez réessayer')
                    print('Rappel des joueurs inscrit:\n')
                    self.view.display_tournament_players(tournament)
                    self.subscribe_player(tournament)

                pass

            case 2:
                """Créer un nouveau joueur"""
                pass

            case 3:
                """Revenir au menu principal"""

    """Générer les rounds"""
