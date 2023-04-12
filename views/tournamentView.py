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
        # self.atts['roundsList'] = input('Nom du tournoi')
        # self.atts['playersList'] = input('Nom du tournoi')
        atts['notes'] = input('Notes du/de la directeur/rice du tournoi\n')  
        return atts