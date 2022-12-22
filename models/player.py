from tinydb import TinyDB

from dataclasses import dataclass

from controllers.user_manager import ControllerPlayer

MAX_PLAYERS_NUMBER = 3


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
        data_players = TinyDB('data_players.json', indent=4)
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
        data_players.insert(serialized_player)

    def create_list_players():
        list_players = []
        for _ in range(MAX_PLAYERS_NUMBER):
            player = Player.save_player_in_db()
            list_players.append(player)
            return list_players




    # def generate_pair():
    #     list_pair_player = Player.create_list_players()
    #     list_player_sorted = sorted(list_pair_player)
    #     print(list_player_sorted)


