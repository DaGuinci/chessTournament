class CreateTournamentView:

    def askUserForTournamentInfos(self):
        self.atts = {}
        print('\nBien, créons notre tournoi\n')
        self.atts['name'] = input('Nom du tournoi\n')
        self.atts['location'] = input('Lieu\n')
        self.atts['startDate'] = input('Date de début\n')
        self.atts['endDate'] = input('Date de fin\n')
        self.atts['numberOfRounds'] = input('Nombre de tours\n')
        self.atts['currentRound'] = input(
            'Numéro du tour en cours (0 pour la création d\'un nouveau tournoi)\n'
            )
        # self.atts['roundsList'] = input('Nom du tournoi')
        # self.atts['playersList'] = input('Nom du tournoi')
        self.atts['notes'] = input('Notes du/de la directeur/rice du tournoi\n')  

        return self.atts