"""Classe de controleur de tournois"""
from .menuController import MenuController
from .dataController import DataController
from models.tournament import Tournament
from views.tournamentView import TournamentView

class TournamentController:
    def __init__(self):
        self.tournaments = []
        self.data_controller = DataController()
        self.init_tournaments()

    """chargement initial des tournois à l'ouverture du programme"""
    def init_tournaments(self):
        tournaments = self.data_controller.load_tournaments()
        for tournament in tournaments:
            t = Tournament(tournament)
            self.tournaments.append(t)

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

    """Processus de création d'un tournoi"""
    def create_tournament(self):
        """Obtenir les infos pour création d'un tournoi"""
        view = TournamentView()
        atts = view.ask_user_for_new()
        # Vérifier le numéro du tour en cours
        atts['roundsList'] = []
        atts['playersList'] = []

        """Création du tournoi"""
        tournament = Tournament(atts)
        self.tournaments.append(tournament)
        self.data_controller.save_tournaments(self.tournaments)
        print('\nTournoi créé.')

    """Sélection d'un tournoi"""
    def select_tournament(self):
        menu = MenuController('select_tournament', self.tournaments)
        choice = menu.ask_user()

        if choice < len(self.tournaments):
            pass

