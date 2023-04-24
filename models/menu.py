class Menu:

    """Initialize a menu
    atts is a dictionary, including :
    title : str
    intro : str
    entries : list
    """

    def __init__(self, menu_name='default', atts={}):
        match menu_name:
            case 'default':
                self.title = 'Menu title'
                self.intro = 'Menu intro'
                self.entries = []

            case 'main_menu':
                self.title = 'Menu principal'
                self.intro = 'Que souhaitez vous faire ?'
                self.entries = [
                    'Créer / Modifier / Jouer un tournoi',
                    'Enregistrer un nouveau joueur',
                    'Afficher la liste des joueurs'
                ]

            case 'main_tournament':
                self.title = 'Menu gestion tournois'
                self.intro = 'Que souhaitez vous faire ?'
                self.entries = [
                    'Créer un tournoi',
                    'Modifier ou jouer un tournoi',
                    'Revenir au menu principal'
                ]

            case 'select_tournament':
                self.title = 'Liste des tournois'
                self.intro = 'Veuillez sélectionner un tournoi'
                self.entries = atts['tournaments']
                if self.entries[- 1] != 'Revenir au menu principal':
                    self.entries.append('Revenir au menu principal')

            case 'modify_tournament':
                tournament = str(atts['tournament'])
                self.title = 'Menu modifier le tournoi ' + tournament
                self.intro = 'Que souhaitez vous faire ?'
                self.entries = [
                    'Inscrire un joueur',
                    'Jouer le tournoi',
                    'Afficher les détails du tournoi',
                    'Revenir au menu principal'
                ]

            case 'subscribe_player':
                tournament = str(atts['tournament'])
                self.title = 'Inscrire un joueur au tournoi ' + tournament
                self.intro = 'Que souhaitez vous faire ?'
                self.entries = [
                    'Inscrire un joueur existant',
                    'Créer un nouveau joueur',
                    'Revenir au menu principal'
                ]

            case 'play_game':
                self.title = 'Entrer le résultat d\'un match'
                self.intro = 'Quel match souhaitez-vous entrer ?'
                self.entries = atts['games']

            case 'winner_select':
                self.title = 'Selection du gagnant'
                self.intro = 'Qui a gagné le match ?'
                self.entries = atts['players']

            case _:
                self.title = 'Menu title'
                self.intro = 'Menu intro'
                self.entries = []
