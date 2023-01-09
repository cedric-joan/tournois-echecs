from tinydb import TinyDB, where
from tinydb.operations import add
from dataclasses import dataclass

from controllers.user_manager import ControllerPlayer

MENU_SCORE = """Choisissez parmi les 3 options suivantes:
0: Perdant
0,5: Match nul
1: Gagnant
Votre choix:  """


MAX_PLAYERS_NUMBER = 8

@dataclass
class Player:
    last_name :str
    first_name :str
    birthday :str
    genre :str
    rank :str
    score:float

    data_base = TinyDB('data_base.json', indent=4)
    player_db = data_base.table("player")

    def create_player():
        input_player = ControllerPlayer.input_controller_player()
        return input_player
        
    def save_player_in_db():
        player = Player.create_player()
        last_name = player[0]
        first_name = player[1]
        birthday = player[2]
        genre = player[3]
        rank = player[4]
        score = 0.0

        serialized_player = {
            "last_name": last_name,
            "first_name": first_name,
            "birthday": birthday,
            "genre": genre,
            "rank": rank,
            "score": score,
        }
        Player.player_db.insert(serialized_player),

    def create_list_players():
        list_players = []
        i = 0
        while i < MAX_PLAYERS_NUMBER:
            player = Player.save_player_in_db()
            list_players.append(player)
            i += 1
            return list_players


    def get_all_players():
        return Player.player_db.all()
        

    def players_sorted_alphabetically():
        list_all_players = Player.player_db.all()
        players_alphabet = sorted(list_all_players, key=lambda player: player["last_name"])
        return players_alphabet    

    # def list_top_of_ranking():
    #     top_rank = Player.sort_players_by_rank()
    #     return top_rank[:4]

    # def list_bottom_of_ranking():
    #     bottom_rank = Player.sort_players_by_rank()
    #     return bottom_rank[5:9]    
    

    def generate_list_pair_round_1():
        pair_of_players = Player.get_all_players()
        return pair_of_players[::4],pair_of_players[1::4],pair_of_players[2::4],pair_of_players[3::4]

              
    def update_rank():
        name_player = input("")
        rank_player = input("")
        Player.player_db.update(rank_player), where("last_name") == name_player
   
        
    def check_score():
        score = input("")
        while score not in ["0", "0.5", "1"] or score == "":
            score = input("\nVous n'avez pas saisi une valeur valide:  ")
            continue
        return float(score)        

    def update_score_players():
        all_players = Player.get_all_players()
        i = 1
        for players in all_players:
            players = players["last_name"]
            print(f"\nEntrez le score de {players}: ")
            Player.player_db.update({"score": Player.check_score()}, doc_ids=[i])
            i += 1

    # def update_score_players():
    #     all_players = Player.get_all_players()
    #     i = 1
    #     for players in all_players:
    #         players = players["last_name"]
    #         print(f"\nEntrez le score de {players}: ")
    #         Player.player_db.update(add({"score": (0.0 + Player.check_score())},  doc_ids=[i]))
    #         i += 1    


    #         # Player.player_db.update({"score": Player.check_score()}, doc_ids=[i])