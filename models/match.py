from dataclasses import dataclass
import player

players = player.Player.new_players

@dataclass
class Match():
       
    def get_pair_players():
       list_players =  []
       for player in players:
        list_players.append(player)
        print(list_players)

        

    