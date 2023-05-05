import random
from models.tournamentRound import TournamentRound
"""Classe tournoi : nom du tournoi, liste de joueurs inscrits"""


class Tournament:
    """Initialisation du tournoi
    atts est un dictionnaire comprenant :
            name,
            location,
            start_date,
            end_date,
            number_of_rounds = 4,
            current_round,
            rounds,
            players,
            players_ids,
            players_scores,
            notes,
            rounds
    """
    def __init__(self, atts):
        self.name = atts['name']
        self.location = atts['location']
        self.start_date = atts['start_date']
        self.end_date = atts['end_date']
        # mettre le nombre de tours par défaut à 4
        self.number_of_rounds = 4
        if type(atts['number_of_rounds']) != int:
            if atts['number_of_rounds'].isdigit():
                atts['number_of_rounds'] = int(atts['number_of_rounds'])
            else:
                # Fixer le nombre de tours par defaut à 4
                atts['number_of_rounds'] = 4
        if atts['number_of_rounds'] > 0:
            self.number_of_rounds = atts['number_of_rounds']
        else:
            # Fixer le nombre de tours par defaut à 4
            atts['number_of_rounds'] == 4
        if atts['current_round'] == '':
            self.current_round = 0
        else:
            self.current_round = atts['current_round']
        if 'players' in atts:
            self.players = atts['players']
        else:
            self.players = []
        if 'players_ids' in atts:
            self.players_ids = atts['players_ids']
        else:
            self.players_ids = []
        if 'players_scores' in atts and len(atts['players_scores']) != 0:
            self.players_scores = atts['players_scores']
        else:
            self.players_scores = {}
        self.notes = atts['notes']
        self.rounds = []
        if len(atts['rounds']) > 0:
            for tournament_round in atts['rounds']:
                one_round = TournamentRound(tournament_round)
                self.rounds.append(one_round)

    # Ajout de joueurs à la liste des inscrits
    def add_player(self, player):
        self.players.append(player)

    def get_player_score(self, idne):
        for id, score in self.players_scores.items():
            if id == idne:
                return score

    # Génération du premier round
    def generate_first_round(self):
        atts = {
            'tournament': self.name,
            'name': 'Round 1',
            'games': [],
            'start': '',
            'end': ''
        }
        # Créer stock joueurs et le tableau des scores
        players_stock = []
        for player in self.players:
            # self.players_scores[player.idne] = 0
            players_stock.append(player)

        while len(players_stock) > 0:
            # Désigner aléatoirement un joueur
            player_1 = random.choice(players_stock)

            # Le retirer du stock
            players_stock.remove(player_1)

            # désigner un autre
            player_2 = random.choice(players_stock)
            players_stock.remove(player_2)
            game = (
                [str(player_1.idne), 0],
                [str(player_2.idne), 0],
            )
            atts['games'].append(game)
        tournament_round = TournamentRound(atts)
        self.rounds.append(tournament_round)
        self.current_round = 1
        # créer le tableau de scores

    def has_been_played(self, game):
        player_1 = game[0][0]
        player_2 = game[1][0]

        # créer la liste des joueurs joués par le joueur 1
        played = []
        for one_round in self.rounds:
            for played_game in one_round.games:
                if player_1 == played_game[0][0]:
                    played.append(played_game[1][0])
                if player_1 == played_game[1][0]:
                    played.append(played_game[0][0])

        # Vérifier si le joueur 2 est dans la liste
        if player_2 in played:
            return True
        return False

    def generate_next_round(self):
        atts = {
            'tournament': self.name,
            'name': 'Round {}'.format(self.current_round),
            'games': [],
            'start': '',
            'end': ''
        }
        print('nouveau round !')
        # classer les joueurs par score
        new_ranking = sorted(
            self.players_scores.items(),
            key=lambda x: x[1],
            reverse=True
            )
        self.players_scores = {}
        for player in new_ranking:
            self.players_scores[player[0]] = player[1]

        # créer une copie de players par score
        players_stock = []
        for player in self.players_scores:
            players_stock.append(player)

        # créer les nouveau matchs
        while len(players_stock) > 2:
            game = (
                [players_stock[0], 0],
                [players_stock[1], 0],
            )

            # vérifier si le match a déjà été joué
            i = 0
            all_were_played = False
            while self.has_been_played(game) and not all_were_played:
                if i < len(players_stock) - 1:
                    game = (
                        [players_stock[0], 0],
                        [players_stock[1 + i], 0]
                    )
                    i += 1
                else:
                    # cas où tous les matchs ont été joués:
                    all_were_played = True
                    game = (
                        [players_stock[0], 0],
                        [players_stock[1], 0],
                    )

            players_stock.remove(game[1][0])
            players_stock.remove(game[0][0])
            atts['games'].append(game)

        # mettre les scores du round à 0
        game = (
            [players_stock[0], 0],
            [players_stock[1], 0],
        )
        atts['games'].append(game)
        tournament_round = TournamentRound(atts)
        self.rounds.append(tournament_round)

    def enter_game_result(self, game_id, winner_id):
        current_round = self.rounds[self.current_round - 1]
        game = current_round.games[game_id]

        # entrer un gagnant
        if winner_id < 2:
            player_id = game[winner_id][0]
            #  ajouter les points au gagnant
            game[winner_id][1] += 1
            self.players_scores[player_id] += 1

        # cas d'égalité
        else:
            game[0][1] += 0.5
            game[1][1] += 0.5
            #  ajouter les points aux joueurs
            self.players_scores[game[0][0]] += 0.5
            self.players_scores[game[1][0]] += 0.5

    def json_serialize(self):
        players = []
        if len(self.players) > 0:
            for player in self.players:
                players.append(player.idne)

        # JSONiser les rounds
        json_rounds = []
        for one_round in self.rounds:
            one_round.json_serialize()
            json_rounds.append(one_round.atts)

        self.atts = {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number_of_rounds': self.number_of_rounds,
            'current_round': self.current_round,
            'rounds': json_rounds,
            'players_ids': players,
            'players_scores': self.players_scores,
            'notes': self.notes,
        }

    def json_unserialize(self, json_datas):
        self.name = json_datas['name'],
        self.location = json_datas['location'],
        self.start_date = json_datas['start_date'],
        self.end_date = json_datas['end_date'],
        self.number_of_rounds = json_datas['number_of_rounds'],
        self.current_round = json_datas['current_round'],
        self.rounds = json_datas['rounds'],
        self.players_ids = json_datas['players_id'],
        self.players_scores = json_datas['players_scores'],
        self.notes = json_datas['notes'],
        self.rounds = json_datas['rounds']

    def __str__(self):
        return self.name
