from tinydb import TinyDB, where

from datetime import datetime
from operator import itemgetter

from dataclasses import dataclass
from models.player import Player
from models.match import Match
from controllers.tournament_manager import ControllerRound


@dataclass
class Rounds:
    name = str
    start: str
    heure_debut: str
    end: str
    heure_fin: str
    list_matchs = []

    data_base = TinyDB('data_base.json', indent=4)
    rounds_db = data_base.table("rounds")

    def date_time_round():
        date = datetime.now()
        day = date.strftime("%d %B %Y")
        hour = date.strftime("%HH %Mm %Ss")
        return day,hour  


    def create_round():
        print("\n")
        print("  Début du tour ")
        name = input("\n⚜  Ajouter un nom  ⚜ : ")
        return name

    def make_round(lists_of_pair):
        lists_matchs = []
        i = 0
        while i < len(lists_of_pair):
            for (player_a, player_b) in lists_of_pair:
                pairs = ControllerRound.generate_match(player_a, player_b)
                lists_matchs.append(pairs)
                i += 1
            end = Rounds.date_time_round()
            print(f"\nfin du Round le {end[0]} à {end[1]}")
        return lists_matchs


    def first_match():
        return 

    def second_round():
        round_2 = Rounds.make_round(Player.associate_players())
        Rounds.rounds_db.insert({"list_match_2": round_2})
        Player.update_score_players()

        return 

    def third_round():
        pass

    def fourth_round():
        Player.generate_list_pair_round_1()



# créer une méthode qui regroupe toutes les autres.
    def save_round():
        start = Rounds.date_time_round()
        name = Rounds.create_round()
        round_1 = Rounds.make_round(Player.generate_list_pair_round_1())
        end = Rounds.date_time_round()

        serialized_round = {
            "round_name": name,
            "start": start,
            "end": end,
            "list_match_1": round_1,
            # "list_match_2": round,
            # "list_match_3": round,
            # "list_match_4": round,
        }
        Rounds.rounds_db.insert(serialized_round)
        Player.update_score_players()

    def list_players_by_match():
        list_players = Rounds.rounds_db.all()
        for players in list_players:
            return players["list_match_1"]
                

    # def list_matchs_in_db():
    #     list_players = Rounds.rounds_db.all()
    #     for players in list_players:
    #         sort_player = sorted(players["list_matchs"])
    #         return sort_player
                
    def sort_players_by_points():
        list_matchs_db = Rounds.list_matchs_in_db()
        for match_player in list_matchs_db:
            print(match_player)
            player = sorted(match_player)
            print(player)

          