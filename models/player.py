from tinydb import TinyDB
from tinydb.operations import add
import random
from views.views_players import ViewsPlayers   

class Player:

    data_base = TinyDB('data_base.json', indent=4)
    player_db = data_base.table("player")

    """ Classe servant a créer une instance de joueur."""
    def __init__(self, views,
                last_name="",
                first_name="", 
                birthday="",
                genre="", 
                rank="0", 
                score="0.0",
                ):
        self.last_name = last_name,
        self.first_name = first_name,
        self.birthday = birthday,
        self.genre = genre,
        self.rank = rank,
        self.score = score
        self.views = views

    def save_player_in_db(self):
        """ Methode servant à serialiser une instance de joueur. """
        serialized_player = {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "genre": self.genre,
            "rank": self.rank,
            "score": self.score,
        }
        Player.player_db.insert(serialized_player),

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

    def update_score_players():
        """ Methode servant a mettre à jour le score d'un joueur."""
        all_players = Player.player_db.all()
        views = ViewsPlayers()
        i = 1
        for players in all_players:
            players = players["last_name"]
            views.print_name(players)
            score_player = views.check_score()
            Player.player_db.update(add("score", + score_player), doc_ids=[i])
            i += 1 

    def update_rank():
        """ Methode servant a mettre à jour le classement d'un joueur."""
        views = ViewsPlayers()
        id = views.check_ids()
        return Player.player_db.update({"rank": views.check_rank()}, doc_ids=[id])

    def players_sorted_alphabetically():
        """ Methode servant a trier les joueurs par ordre alphabétique.
        return : str nom des joueurs """
        views = ViewsPlayers()
        db_all = Player.player_db.all()
        players = sorted(db_all, key=lambda player: player["last_name"], reverse=False)
        for player in players:
            player = player["last_name"]
            views.print_name(player) 