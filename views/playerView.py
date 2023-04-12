class PlayerView:
    
    """Obrenir les infos pour création d'un joueur"""
    def ask_user_for_new(self):
        atts = {}
        print('=============================')
        print('Création d\'un joueur')
        print('=============================')
        print('\n')
        atts['firstName'] = input('Prénom\n')
        atts['lastName'] = input('Nom de famille\n')
        atts['birthDate'] = input('Date de naissance\n')
        atts['idne'] = input('Identifiant national\n')
        return atts

    """Affichage de la liste de joueurs"""
    def display_players(self, players):
        print('=============================')
        print('Liste des joueurs enregistrés')
        print('=============================')
        print('\n')
        for player in players:
            print(player)