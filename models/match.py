from dataclasses import dataclass

from models.player import Player


@dataclass
class Match():
    player_a: str
    player_b: str
    score_player_a : str
    score_player_a : str


    # def generate_pair_of_players():
    #     pair_of_players = Player.sort_players_by_rank()
    #     player_a = pair_of_players[0]
    #     player_b = pair_of_players[5]
    #     list_of_pair = []
    #     list_of_pair.append(player_a)
    #     list_of_pair.append(player_b)
    #     print(list_of_pair)

    def generate_pair_of_players():
        pair_of_players = Player.sort_players_by_rank()
        return pair_of_players[::5]


    


