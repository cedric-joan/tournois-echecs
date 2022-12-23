# from dataclasses import dataclass

from tinydb import TinyDB
data_base = TinyDB('data_base.json', indent=4)
player_db = data_base.table("player")

# @dataclass
# class Match():
#     player_a: str
#     player_b: str


def pair_of_player():
    players = player_db.all()
    for player in players:
        print(player)
    


if __name__ == "__main__":  
    pair_of_player()          