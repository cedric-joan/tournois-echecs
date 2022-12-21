from tinydb import TinyDB

from dataclasses import dataclass

from controllers.user_manager import ControllerUser

MAX_PLAYERS_NUMBER = 3

data_players = TinyDB('data_players.json', indent=4)

@dataclass
class Player:
    last_name :str
    first_name :str
    birthday :str
    sexe :str
    rank :str
    score :str


    def create_players():
        user = ControllerUser.input_controller_user()
        player = {
                "last_name": user.last_name,
                "first_name": user.first_name,
                "birthday": user.birthday,
                "sexe": user.sexe,
                "rank": user.rank,
            }
        data_players.insert(player)    

        return user

    # def save_player(self):
    #     data_players.insert(
    #         {
    #             "last_name": self.last_name,
    #             "first_name": self.first_name,
    #             "birthday": self.birthday,
    #             "sexe": self.sexe,
    #             "rank": self.rank,
    #         }
    #     )


    def create_list_players():
        list_players = []
        for _ in range(MAX_PLAYERS_NUMBER):
            player = Player.create_players()
            list_players.append(player)
            print(list_players)




    # def generate_pair():
    #     list_pair_player = Player.create_list_players()
    #     list_player_sorted = sorted(list_pair_player)
    #     print(list_player_sorted)


