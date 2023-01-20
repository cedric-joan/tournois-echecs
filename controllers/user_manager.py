from models.player import Player
from views.views_players import ViewsPlayers

class UserManager:
    def __init__(self, list_players, player):
        self.list_players = list_players
        self.player = player

    def create_player():
        """ Methode servant a créer un joueur."""
        player = Player()
        ViewsPlayers.input_player(player)
        player.save_player_in_db()      

    def create_list_players():
        """ Methode servant a créer plusieurs joueurs."""
        list_players = []
        for player in range(1, 9):
            player = Player()
            ViewsPlayers.input_player(player)
            list_players.append(player)
            player.save_player_in_db()      

           