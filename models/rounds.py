from tinydb import TinyDB

from dataclasses import dataclass
from models.player import Player
from controllers.tournament_manager import ControllerRound

from datetime import datetime



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
                pair = ControllerRound.init_round(player_a, player_b)
                lists_matchs.append(pair)
                i += 1
            end = Rounds.date_time_round()
            print(f"fin du Round le {end[0]} à {end[1]}")
        return lists_matchs


    def first_round():
        round_1 = Rounds.make_round(Player.generate_list_pair_round_1())
        return round_1

    def second_round():
        pass

    def third_round():
        pass

    def fourth_round():
        pass

# créer une méthode qui regroupe toutes les autres.
    def save_round():
        start = Rounds.date_time_round()
        name = Rounds.create_round()
        list_matchs = Rounds.make_round()
        end = Rounds.date_time_round()

        serialized_round = {
            "round_name": name,
            "start": start,
            "end": end,
            "list_matchs": list_matchs,
        }
        Rounds.rounds_db.insert(serialized_round)

    def sort_players_by_points():
            list_players = Rounds.rounds_db.all()
            for player in list_players:
                print(player["list_matchs"])


    # def sort_players_by_points():
    #     list_players = Rounds.rounds_db.all()
    #     for player in list_players:
    #         players = sorted(player, key=lambda list_matchs: list_matchs[1])
    #         print(players)