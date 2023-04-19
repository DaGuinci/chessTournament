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
            self.tournaments.append(t)

    """Sauvegarde de l'état"""
    def save(self):
        self.data_controller.save_tournaments(self.tournaments)
    
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
                for player_iter in players:
                    if player_id == player_iter.idne:
                        player_exists = True
                        player = player_iter

                """Vérfifier que le joueur n'est pas déjà inscrit"""
                player_yet_in_tournament = False
                for player_in_tournament in tournament.players:
                    if player_id == player_in_tournament.idne:
                        player_yet_in_tournament = True
                
                """Inscrire le joueur"""
                if player_exists and not player_yet_in_tournament:
                    tournament.add_player(player)
                    self.save()
                    self.view.display_tournament_players(tournament)
                    self.modify_tournament(tournament)
                    #TODO Afficher un message de réussite

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

            case 2:
                """Créer un nouveau joueur"""
                self.player_controller.create_player(tournament)
                self.save()
                self.modify_tournament(tournament)
                #TODO Afficher un message de réussite

            case 3:
                """Revenir au menu principal"""

    """Création d'un tournoi"""
    def create_tournament(self):
        """Obtenir les infos pour création d'un tournoi"""
        atts = self.view.ask_user_for_new()
        # Vérifier le numéro du tour en cours
        atts['rounds'] = []
        atts['players'] = []
        atts['players_ids'] = []
        atts['current_round'] = 0

        tournament = Tournament(atts)
        self.tournaments.append(tournament)
        self.save()
        print('\nTournoi créé.')

    #Préparer et lancer l'affichage de ;'état du tournoi
    def tournament_state(self, tournament):
        datas = {}
        ranking = []
        for player, score in tournament.players_scores.items():
            player_name = self.player_controller.get_player_name_by_id(player)
            ranking.append([player_name, score])
        datas['ranking'] = ranking
        rounds = []
        for one_round in tournament.rounds:
            this_round = {}
            this_round['name'] = one_round.name
            this_round['games'] = []
            rounds.append(this_round)
            for game in one_round.games:
                this_game = {}
                name_1 = self.player_controller.get_player_name_by_id(game[0][0])
                name_2 = self.player_controller.get_player_name_by_id(game[1][0])
                this_game['player_1'] = name_1
                this_game['player_2'] = name_2
                this_game['status'] = game[2]
                this_round['games'].append(this_game)
        datas['rounds'] = rounds
        self.view.display_tournament_state(datas)

    #Proposer de rentrer les résultats d'un match
    def play_game_menu(self, tournament):
        id_round = tournament.current_round - 1
        current_round = tournament.rounds[id_round]
        atts = {}
        games = []
        winner_menu = []
        for game in current_round.games:
            name_1 = self.player_controller.get_player_name_by_id(game[0][0])
            name_2 = self.player_controller.get_player_name_by_id(game[1][0])
            game_repr = name_1 + ' - ' + name_2
            winner_menu.append((name_1, name_2, 'Match nul'))
            games.append(game_repr)
        atts['games'] = games
        menu = MenuController('play_game', atts)
        #TODO vérifier si le match a été joué
        choice = menu.ask_user()
        game_id = choice - 1
        winner_select = winner_menu[game_id]
        atts['players'] = winner_menu[game_id]
        winner_select_menu = MenuController('winner_select', atts)
        winner_id = winner_select_menu.ask_user()
        tournament.enter_game_result(game_id, winner_id - 1)
        self.save()
        self.modify_tournament(tournament)

    def modify_tournament(self, tournament):
        atts = {
            'tournament' : tournament
        }
        menu = MenuController('modify_tournament', atts)
        choice = menu.ask_user()
        match choice:
            case 1:
                self.subscribe_player(tournament)
            case 2:
                """Jouer le tournoi"""
                #TODO Afficher un résumé de l'état du tournoi:
                #round en cours, classement joueurs
                #Si pas de round, créer premier round
                if tournament.current_round == 0:
                    #TODO vérifier nombre de joueurs
                    tournament.generate_first_round()
                    self.save()
                else:
                    #Afficher l'état du round
                    self.tournament_state(tournament)
                    #Proposer d'entrer les résultats de matchs
                    self.play_game_menu(tournament)
                    #TODO Générer le tour suivant
                #Si round, reprendre en l'état
            case 3:
                """Afficher les détails"""
                #Afficher les joueurs inscrits
                self.view.display_tournament_players(tournament)
                self.tournament_state(tournament)
                #TODO Afficher l'état des rounds
                self.modify_tournament(tournament)

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
        self.modify_tournament(self.tournaments[choice - 1])
        """TODO Dernier choix : revenir au menu principal"""

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