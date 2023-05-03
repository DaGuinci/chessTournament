"""Un round possède comme attributs :
un nom(str)
une liste de matchs
horodatage auto debut
horodatage auto fin
"""
from datetime import datetime


class TournamentRound:

    def __init__(self, atts):
        self.tournament = atts['tournament']
        self.name = atts['name']
        self.games = atts['games']
        # Gérer les remplissage auto des horodatages
        if atts['start'] == '':
            # current_dateTime = datetime.now()
            self.start = datetime.now()
        else:
            self.start = datetime.strptime(
                atts['start'], '%Y-%m-%dT%H:%M:%S.%f'
                )
        if atts['end'] == '':
            self.end = ''
        else:
            self.end = datetime.strptime(atts['end'], '%Y-%m-%dT%H:%M:%S.%f')

    def end_round(self):
        current_dateTime = datetime.now()
        self.end = current_dateTime

    # preparer l'affichage des matchs
    def games_repr(self, player_controller):
        datas = {
            'games': [],
            'winner_menu': []
        }
        for game in self.games:
            name_1 = player_controller.get_player_name_by_id(
                game[0][0]
                )
            name_2 = player_controller.get_player_name_by_id(
                game[1][0]
                )
            game_repr = name_1 + ' - ' + name_2
            # Indique si le match a été joué ou non
            if game[0][1] == 0 and game[1][1] == 0:
                game_repr += ' - Á jouer'
            else:
                game_repr += ' - Joué'
            datas['winner_menu'].append((name_1, name_2, 'Match nul'))
            datas['games'].append(game_repr)
        return datas

    # vérifier si le round reste ouvert
    def is_played(self):
        for game in self.games:
            if game[0][1] == 0 and game[1][1] == 0:
                return False
        return True

    def json_serialize(self):
        if self.end == '':
            end = ''
        else:
            end = self.end.strftime('%Y-%m-%dT%H:%M:%S.%f')

        self.atts = {
            'tournament': self.tournament,
            'name': self.name,
            'games': self.games,
            'start': self.start.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'end': end
        }
