from tinydb import TinyDB, where
from datetime import datetime

from views.views_tournament import ViewsTournament
from models.player import Player
from controllers.tournament_manager import ControllerRound

class Rounds:
    """ Classe servant a créer une instance de tour."""
    def __init__(self, name="",start="", day="",hour="", end=""):
        self.name = name
        self.start = start
        self.day = day
        self.end = end
        self.hour = hour

    list_matchs = []
    data_base = TinyDB('data_base.json', indent=4)
    rounds_db = data_base.table("rounds")

    def date_time_round():
        """ Methode servant a générer une date et une heure."""
        date = datetime.now()
        day = date.strftime("%d %B %Y")
        hour = date.strftime("%HH %Mm %Ss")
        return day,hour  

    def generate_round(lists_of_pair):
        """ Methode servant a générer un tour."""
        lists_matchs = []
        i = 0
        while i < len(lists_of_pair):
            for (player_a, player_b) in lists_of_pair:
                pairs = ControllerRound.generate_match(player_a, player_b)
                lists_matchs.append(pairs)
                i += 1
        return lists_matchs

    def first_match():
        """ Methode servant a générer le premier tour."""
        return Rounds.generate_round(Rounds.generate_first_round())

    def next_round():
        """ Methode servant a générer les prochains tours."""
        i = 0
        while i < 3:
            next_round = Rounds.generate_round(Rounds.generate_next_round())
            Rounds.rounds_db.insert({"list_match": next_round})
            Player.update_score_players()
            i += 1

    def save_round():
        """ Methode servant à serialiser une instance de tour. """
        start = Rounds.date_time_round()
        name = ViewsTournament.create_round()
        end = Rounds.date_time_round()
        round_1 = Rounds.first_match()
        serialized_round = {
            "round_name": name,
            "start": start,
            "end": end,
            "list_match": round_1,
        }
        Rounds.rounds_db.insert(serialized_round)
        Player.update_score_players()

    def list_players_by_match():
        """ Methode servant a générer la liste de joueurs par match."""
        display_list_players = []
        list_players = Rounds.rounds_db.all()
        for players in list_players[0]["list_match"]:
            display_list_players.append(players[0][0])
            display_list_players.append(players[1][0])
        list_sorted = sorted(display_list_players)   
        return list_sorted

    def generate_first_round():
        """ Methode servant a générer une liste de paire de joueurs."""
        players = Player.player_db.all()
        return [players[::4], players[1::4], players[2::4], players[3::4]]   

    def generate_next_round():
        """ Methode servant a générer le prochain tour."""
        list_players = Rounds.rounds_db.all()
        i = 0
        for matches in list_players:
            matches = matches["list_match"]
            if matches[i] != matches[i]:
                Player.associate_players()
                i += 1
            else:
                Player.sort_players_score()

            