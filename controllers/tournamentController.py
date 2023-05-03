"""Classe de controleur de tournois"""
from .menuController import MenuController
from .dataController import DataController
from controllers.playerController import PlayerController
from models.tournament import Tournament
from views.tournamentView import TournamentView
import locale
locale.setlocale(locale.LC_TIME, '')


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
            'tournament': tournament
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
                    tournament.players_scores.update({player_id: 0})
                    self.save()
                    self.view.display_tournament_players(tournament)
                    self.modify_tournament(tournament)

                if not player_exists:
                    """TODO générer des messages d'erreur"""
                    print(
                        'Désolé, ce joueur n\'existe pas, veuillez réessayer'
                    )
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

            case 3:
                """Revenir au menu principal"""

    """Création d'un tournoi"""
    def create_tournament(self):
        """Obtenir les infos pour création d'un tournoi"""
        atts = self.view.ask_user_for_new()
        #  Vérifier le numéro du tour en cours
        atts['rounds'] = []
        atts['players'] = []
        atts['players_ids'] = []
        atts['current_round'] = 0

        tournament = Tournament(atts)
        self.tournaments.append(tournament)
        self.save()
        print('\nTournoi créé.')

    # Préparer et lancer l'affichage de ;'état du tournoi
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
            this_round['start'] = one_round.start.strftime(
                '%A %d %b %Y, %H:%M%p'
                )
            if one_round.end == '':
                this_round['end'] = 'Tour en cours'
            else:
                this_round['end'] = one_round.end.strftime(
                    '%A %d %b %Y, %H:%M%p'
                    )
            this_round['games'] = []
            rounds.append(this_round)
            for game in one_round.games:
                this_game = {}
                pl_controller = self.player_controller
                name_1 = pl_controller.get_player_name_by_id(game[0][0])
                name_2 = pl_controller.get_player_name_by_id(game[1][0])
                this_game['player_1'] = name_1
                this_game['player_2'] = name_2
                if game[0][1] == 0 and game[1][1] == 0:
                    this_game['status'] = False
                else:
                    this_game['status'] = True
                this_round['games'].append(this_game)
        datas['rounds'] = rounds
        self.view.display_tournament_state(datas)

    # Proposer de rentrer les résultats d'un match
    def play_game_menu(self, tournament):
        id_round = tournament.current_round - 1
        current_round = tournament.rounds[id_round]
        generate = False
        # vérifier si le round est ouvert
        if current_round.is_played():
            # proposer de clore le round
            if current_round.end == '':
                end_round = self.view.ask_for_end_round()
                if end_round:
                    current_round.end_round()
                    self.save()
                    if tournament.current_round == tournament.number_of_rounds:
                        print('Le tournoi est terminé')
                    else:
                        generate = self.view.ask_for_new_round()
                else:
                    self.modify_tournament(tournament)
            else:
                if tournament.current_round == tournament.number_of_rounds:
                    print('Le tournoi est terminé')
                else:
                    # proposer de commencer le nouveau round si nouveau round
                    generate = self.view.ask_for_new_round()
            if generate:
                tournament.current_round += 1
                tournament.generate_next_round()
                self.save()
                self.modify_tournament(tournament)
        else:
            atts = {}
            games_datas = current_round.games_repr(self.player_controller)
            atts['games'] = games_datas['games']
            winner_menu = games_datas['winner_menu']
            menu = MenuController('play_game', atts)
            # vérifier si le match a été joué
            choice = menu.ask_user()
            game_id = choice - 1
            if not (current_round.games[game_id][0][1] == 0 and
                    current_round.games[game_id][1][1] == 0):
                print('Ce match a déjà été joué.')
                print('Veuillez en sélectionner un autre.')
                self.play_game_menu(tournament)
            else:
                atts['players'] = winner_menu[game_id]
                winner_select_menu = MenuController('winner_select', atts)
                winner_id = winner_select_menu.ask_user()
                tournament.enter_game_result(game_id, winner_id - 1)
                self.save()
                self.modify_tournament(tournament)

    def modify_tournament(self, tournament):
        atts = {
            'tournament': tournament
        }
        menu = MenuController('modify_tournament', atts)
        choice = menu.ask_user()
        match choice:
            case 1:
                """Jouer le tournoi"""
                # Afficher un résumé de l'état du tournoi:
                self.tournament_state(tournament)
                # Si pas de round, créer premier round
                if tournament.current_round == 0:
                    # vérifier nombre de joueurs
                    if len(tournament.players) >= 8:
                        # proposer de créer le premier round
                        generate = self.view.ask_for_new_round()
                        if generate:
                            tournament.generate_first_round()
                            self.save()
                            self.play_game_menu(tournament)
                        else:
                            self.modify_tournament(tournament)
                    else:
                        print('Le nombre de joueurs n\'est pas adapté.')
                        print('Inscrivez des joueurs, svp.')
                        self.modify_tournament(tournament)
                else:
                    # Afficher l'état du round
                    self.tournament_state(tournament)
                    # Proposer d'entrer les résultats de matchs
                    self.play_game_menu(tournament)
            case 2:
                self.subscribe_player(tournament)
            case 3:
                # Afficher les détails
                self.view.dispay_tournament_details(tournament)
                # Afficher les joueurs inscrits
                self.view.display_tournament_players(tournament)
                # Afficher l'état des rounds
                self.tournament_state(tournament)
                self.modify_tournament(tournament)
            case 4:
                self.main_tournament()

    # Menu tournois
    def main_tournament(self):
        tournaments = []
        for t in self.tournaments:
            tournaments.append(t)
        atts = {
            'tournaments': tournaments
        }
        menu = MenuController('tournaments_menu', atts)
        choice = menu.ask_user()

        if choice <= len(self.tournaments):
            self.modify_tournament(self.tournaments[choice - 1])

        # Avant dernier choix : Créer un tournoi
        elif choice == len(self.tournaments) + 1:
            self.create_tournament()

        # Dernier choix : revenir au menu principal
        elif choice == len(self.tournaments) + 2:
            pass
