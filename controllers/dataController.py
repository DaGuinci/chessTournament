"""Méthodes dde lecture et écriture des données en JSON"""
import os
import json


class DataController:
    if not os.path.exists('out/'):
        os.mkdir('out/')

    def is_non_zero_file(self, fpath):
        return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

    def load_tournaments(self):
        file_is_not_empty = self.is_non_zero_file("out/tournaments.json")
        if file_is_not_empty:
            with open(f'{"out/tournaments.json"}', "r") as f:
                tournaments = json.load(f)
            return tournaments
        else:
            return []

    def save_tournaments(self, tournaments):
        datas = []

        if len(tournaments) > 0:
            for tournament in tournaments:
                tournament.json_serialize()
                datas.append(tournament.atts)

            with open(f'{"out/tournaments.json"}', "w") as f:
                """TODO vérifier si besoin d'un json.dump"""
                json.dump(datas, f)

    def load_players(self):
        file_is_not_empty = self.is_non_zero_file("out/players.json")
        if file_is_not_empty:
            with open(f'{"out/players.json"}', "r") as f:
                players = json.load(f)
            return players
        else:
            return []

    def save_players(self, players):
        datas = []

        if len(players) > 0:
            for player in players:
                player.json_serialize()
                datas.append(player.atts)

            with open(f'{"out/players.json"}', "w") as f:
                json.dump(datas, f)
