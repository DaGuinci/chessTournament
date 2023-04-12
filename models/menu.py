class Menu:

    """Initialize a menu
    atts is a dictionary, including :
    title : str
    intro : str
    entries : list
    """

    def __init__(self, menu_name = 'default', atts = []):
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
                self.entries = atts
                if self.entries[- 1] != 'Revenir au menu principal':
                    self.entries.append('Revenir au menu principal')
            
            case other:
                self.title = 'Menu title'
                self.intro = 'Menu intro'
                self.entries = []