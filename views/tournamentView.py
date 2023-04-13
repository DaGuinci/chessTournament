class TournamentView:

    """Obtenir les infos pour création d'un tournoi"""
    def ask_user_for_new(self):
        atts = {}
        print('=============================')
        print('Création d\'un tournoi')
        print('=============================')
        print('\n')
        atts['name'] = input('Nom du tournoi\n')
        atts['location'] = input('Lieu\n')
        atts['startDate'] = input('Date de début\n')
        atts['endDate'] = input('Date de fin\n')
        atts['numberOfRounds'] = input('Nombre de tours\n')
        atts['currentRound'] = input(
            'Numéro du tour en cours (0 pour la création d\'un nouveau tournoi)\n'
            )
        # self.atts['rounds'] = input('Nom du tournoi')
        # self.atts['players'] = input('Nom du tournoi')
        atts['notes'] = input('Notes du/de la directeur/rice du tournoi\n')  
        return atts
    
    def ask_user_for_player_id(self):
        player_id = input('Identifiant national du joueur\n')
        return player_id
    
    def display_tournament_players(self, tournament):
        i = 1
        for player in tournament.players:
            print('Joueur n˚' + str(i) + ' :')
            print('Nom et prénom :')
            print(player.lastName + ' ' + player.firstName)
            print('Identifiant national :')
            print(player.idne, '\n')
            i += 1