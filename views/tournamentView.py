class TournamentView:

    # Obtenir les infos pour création d'un tournoi
    def ask_user_for_new(self):
        atts = {}
        print('=============================')
        print('Création d\'un tournoi')
        print('=============================')
        print('\n')
        atts['name'] = input('Nom du tournoi\n')
        atts['location'] = input('Lieu\n')
        atts['start_date'] = input('Date de début\n')
        atts['end_date'] = input('Date de fin\n')
        atts['number_of_rounds'] = input('Nombre de tours (par défaut : 4) \n')
        atts['notes'] = input('Notes du/de la directeur/rice du tournoi\n')
        return atts

    def ask_user_for_player_id(self):
        player_id = input('Identifiant national du joueur\n')
        return player_id

    def display_tournament_players(self, tournament):
        i = 1
        print('=============================')
        print('Joueurs inscrits')
        print('=============================\n')
        for player in sorted(
                tournament.players, key=lambda player: player.lastName
                ):
            print('Joueur n˚' + str(i) + ' :')
            print('Nom et prénom :')
            print(player.firstName + ' ' + player.lastName)
            print('Identifiant national :')
            print(player.idne, '\n')
            i += 1

    def dispay_tournament_details(self, tournament):
        print('=============================')
        print('Informations du tournoi')
        print('=============================')
        print('\nNom :\n')
        print(tournament.name)
        print('\nLieu :\n')
        print(tournament.location)
        print('\nNombre de tours :\n')
        print(tournament.number_of_rounds)
        print('\nDate de début :\n')
        print(tournament.start_date)
        print('\nDate de fin :\n')
        print(tournament.end_date)
        print('\nNotes :\n')
        print(tournament.notes)

    def display_tournament_state(self, datas):
        print('=============================')
        print('État du tournoi')
        print('=============================')
        print('\nClassement :\n')
        for player in datas['ranking']:
            print(player[0], player[1])

        print('\nRounds :')
        for one_round in datas['rounds']:
            print('\n' + one_round['name'])
            print('Commencé le:')
            print(one_round['start'], '\n')
            print('Terminé le:')
            print(one_round['end'], '\n')
            for game in one_round['games']:
                status = 'Joué' if game['status'] else 'À jouer'
                print('{} - {} - {}'.format(
                    game['player_1'], game['player_2'], status)
                )

    def ask_for_new_round(self):
        response = input('Souhaitez-vous commencer le nouveau round ? (o/n)\n')
        if response == 'o':
            return True
        elif response == 'n':
            return False
        else:
            print('Désolé, votre réponse n\'est pas valide.')
            print('Veuillez réessayer.')
            return (self.ask_for_new_round())

    def ask_for_end_round(self):
        print('\nTous les matchs du round sont joués.')
        response = input('Souhaitez-vous clore le round ? (o/n)\n')
        if response == 'o':
            return True
        elif response == 'n':
            return False
        else:
            print('Désolé, votre réponse n\'est pas valide.')
            print('Veuillez réessayer.')
            return (self.ask_for_end_round())
