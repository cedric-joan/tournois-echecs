# from tinydb import TinyDB

from dataclasses import dataclass

# from models.player import Player



@dataclass
class Match:
    player_a: str
    player_b: str
    score_a: float
    score_b: float
    

    # data_base = TinyDB('data_base.json', indent=4)
    # matchs_db = data_base.table("players_matchs")   

    def list_pair(player_a,score_a, player_b, score_b):
        list_player_a = []
        list_player_b = []
        tuple_pair = ()
        list_player_a = player_a, score_a
        list_player_b = player_b, score_b
        tuple_pair = list_player_a, list_player_b
        return tuple_pair

    # def save_players_match_in_db():
    #     player = Player.get_all_players()
    #     player_1 = player[0]
    #     player_2 = player[1]
    #     player_3 = player[2]
    #     player_4 = player[3]
    #     player_5 = player[4]
    #     player_6 = player[5]
    #     player_7 = player[6]
    #     player_8 = player[7]

    #     serialized_player_for_match = {
    #         "player_1": player_1,
    #         "player_2": player_2,
    #         "player_3": player_3,
    #         "player_4": player_4,
    #         "player_5": player_5,
    #         "player_6": player_6,
    #         "player_7": player_7,
    #         "player_8": player_8,
    #     }
    #     Match.matchs_db.insert(serialized_player_for_match),


    # def get_all_players_match_in_db():
    #     all_players_match = Match.matchs_db.all()
    #     for all_players in all_players_match:
    #         return all_players


        
    # def generate_list_pair_1():
    #     pair_of_players = Match.matchs_db.all()
    #     list_pair_1 = []
    #     list_pair_2 = []
    #     list_pair_3 = []
    #     list_pair_4 = []
    #     for players in pair_of_players:
    #         list_pair_1.append(players["player_1"])
    #         list_pair_1.append(players["player_5"])
    #         list_pair_2.append(players["player_2"])
    #         list_pair_2.append(players["player_6"])
    #         list_pair_3.append(players["player_3"])
    #         list_pair_3.append(players["player_7"])
    #         list_pair_4.append(players["player_4"])
    #         list_pair_4.append(players["player_8"])
    #         return list_pair_1, list_pair_2, list_pair_3, list_pair_4


    # def get_players_round():
    #     all_players = Match.matchs_db.all()
    #     for player in all_players:
    #         return player

    





                               

