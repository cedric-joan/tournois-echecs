from dataclasses import dataclass

from controllers.tournament_manager import ControllerTournament

SEPARATOR = "-" * 60
ROUND_DEFAULT = 4

@dataclass
class Tournament:
    name: str
    place: str
    date_now: str
    round_number = 4
    list_players: str
    time: str
    note: str

    def create_tournament():
        tournament = ControllerTournament.input_controller_tournament()
        return tournament
        


        





        
        
