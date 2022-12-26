from tinydb import TinyDB

from dataclasses import dataclass

from controllers.user_manager import ControllerPlayer

MAX_PLAYERS_NUMBER = 3


data_base = TinyDB('data_base.json', indent=4)
player_db = data_base.table("player")
@dataclass
class Player:
    last_name :str
    first_name :str
    birthday :str
    genre :str
    rank :str
    # score :str

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

        serialized_player = {
            "last_name": last_name,
            "first_name": first_name,
            "birthday": birthday,
            "genre": genre,
            "rank": rank,
        }
        player_db.insert(serialized_player)

    def create_list_players():
        list_players = []
        for _ in range(MAX_PLAYERS_NUMBER):
            player = Player.save_player_in_db()
            list_players.append(player)
            return list_players

    def get_all_players():
        list_player = player_db.all()
        return list_player


    def sort_players_by_rank():
        list_all_players = Player.get_all_players()
        players_rank = sorted(list_all_players, key=lambda player: player["rank"])
        return players_rank

    def players_sorted_alphabetically():
        list_all_players = Player.get_all_players()
        players_alphabet = sorted(list_all_players, key=lambda player: player["last_name"])
        print(players_alphabet)    

    def list_top_of_ranking():
        top_rank = Player.sort_players_by_rank()
        return top_rank[:4]

    def list_bottom_of_ranking():
        bottom_rank = Player.sort_players_by_rank()
        return bottom_rank[5:9]    
    