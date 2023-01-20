from random import randint

from models.match import Match
from views.views_tournament import InputTournament
from models.tournament import Tournament

RESULT_TO_FIND = randint(0, 2)
SEPARATOR = "-" * 60

class TournamentManager:
    def __init__(self, tournament ):
        self.tournament = tournament

    def create_tournament():
        """ Methode servant a créer un nouveau tournois."""
        tournament = Tournament()
        InputTournament.start_tournament(tournament)
        tournament.save_tournament()

class ControllerRound:

    def generate_match(player_a, player_b):
        """ Methode servant a générer un match."""
        InputTournament.start_match()
        player_a = player_a["last_name"]
        player_b = player_b["last_name"]
        winner = 2
        loser = 1
        if RESULT_TO_FIND == winner:
            print(f" Le joueur {player_a} a gagné \n Le joueur {player_b} a perdu")
            score_a = 1.0
            score_b = 0.0
            result = Match.list_pairs(player_a, score_a, player_b, score_b)
            return result
        if RESULT_TO_FIND == loser:
            print(f" Le joueur {player_b} a gagné \n Le joueur {player_a} a perdu")
            score_b = 1.0
            score_a = 0.0
            result = Match.list_pairs(player_a, score_a, player_b, score_b)
            return result
        else:
            print(f" Les joueurs {player_a} et {player_b} ont fait match nul")
            score_a = 0.5
            score_b = 0.5
            result = Match.list_pairs(player_a, score_a, player_b, score_b)
            return result