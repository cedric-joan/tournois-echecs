from tinydb import TinyDB
from tinydb.operations import add
import random

from controllers.menu_manager import MenuManager
from controllers.user_manager import ControllerPlayer

PLAYERS_NUMBER = 8

class Player:
    """ Classe servant a créer une instance de joueur."""
    def __init__(self, last_name="", first_name="", birthday="", genre="", rank="", score=0.0):
        self.last_name = last_name,
        self.first_name = first_name,
        self.birthday = birthday,
        self.genre = genre,
        self.rank = rank,
        self.score = score

    data_base = TinyDB('data_base.json', indent=4)
    player_db = data_base.table("player")

    def create_player():
        """ Methode servant a ajouter un joueur."""
        return ControllerPlayer.input_controller_player()

    def save_player_in_db():
        """ Methode servant à serialiser une instance de joueur. """
        player = ControllerPlayer.input_controller_player()
        last_name = player[0]
        first_name = player[1]
        birthday = player[2]
        genre = player[3]
        rank = player[4]
        score = player[5]
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
        """ Methode servant a créer plusieurs joueurs."""
        list_players = []
        i = 0
        while i < PLAYERS_NUMBER:
            player = Player.save_player_in_db()
            list_players.append(player)
            i += 1

    def update_score_players():
        """ Methode servant a mettre à jour le score d'un joueur."""
        all_players = Player.player_db.all()
        i = 1
        for players in all_players:
            players = players["last_name"]
            print(f"\nEntrez le score de {players}: ")
            score_player = MenuManager.check_score()
            Player.player_db.update(add("score", + score_player), doc_ids=[i])
            i += 1

    def update_rank():
        """ Methode servant a mettre à jour le classement d'un joueur."""
        id = MenuManager.check_ids()
        return Player.player_db.update({"rank": ControllerPlayer.check_rank()}, doc_ids=[id])

    def sort_players_score():
        """ Methode servant a trier les joueurs par score."""
        list_players = Player.player_db.all()
        for players in list_players:
            players = players["score"]
            if players == 0.5:
                random.shuffle(list_players)
                return list_players
            if players == 1.0:
                random.shuffle(list_players)
                return list_players
            else:
                return Player.associate_players() 

    def associate_players():
        """ Methode servant a associer les joueurs."""
        list_db = Player.player_db.all()
        players = sorted(list_db, key=lambda player: player["score"])
        return [players[0:2], players[2:4], players[4:6], players[6:8]] 