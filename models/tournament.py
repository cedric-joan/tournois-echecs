from tinydb import TinyDB

from dataclasses import dataclass

from controllers.tournament_manager import ControllerTournament


SEPARATOR = "-" * 60
ROUND_DEFAULT = 4

data_base = TinyDB('data_base.json', indent=4)
tournament_db = data_base.table("tournament")

@dataclass
class Tournament:
    name: str
    place: str
    date: str
    time: str
    note: str

    def create_tournament():
        tournament = ControllerTournament.input_controller_tournament()
        return tournament
        
    def save_tournament_in_db():
        tournament = Tournament.create_tournament()
        name = tournament[0]
        place = tournament[1]
        date = tournament[2]
        time = tournament[3]
        note = tournament[4]

        serialized_tournament = {
            "name": name,
            "place": place,
            "date": date,
            "time": time,
            "note": note,
        }
        tournament_db.insert(serialized_tournament)
        
    def start_tournament():
        Tournament.save_tournament_in_db()




        
        
