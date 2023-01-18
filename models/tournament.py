from tinydb import TinyDB

from controllers.tournament_manager import ControllerTournament

SEPARATOR = "-" * 60

class Tournament:
    """ Classe servant a créer une instance de tournoi."""
    def __init__(self, name,place, date, time, note, rounds):
        self.name = name
        self.place = place
        self.date = date
        self.time = time
        self.note = note
        self.rounds = rounds
    
    data_base = TinyDB('data_base.json', indent=4)
    tournament_db = data_base.table("tournament")

    def start_tournament():
        """ Methode servant à serialiser une instance de tournoi. """
        tournament = ControllerTournament.input_controller_tournament()
        name = tournament[0]
        place = tournament[1]
        date = tournament[2]
        time = tournament[3]
        note = tournament[4]
        rounds = 4
        serialized_tournament = {
            "name": name,
            "place": place,
            "date": date,
            "time": time,
            "note": note,
            "rounds": rounds,
        }
        Tournament.tournament_db.insert(serialized_tournament)
        
    


    

        
        
