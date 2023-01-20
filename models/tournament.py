from tinydb import TinyDB

SEPARATOR = "-" * 60

class Tournament:

    data_base = TinyDB('data_base.json', indent=4)
    tournament_db = data_base.table("tournament")
    """ Classe servant a créer une instance de tournoi."""
    def __init__(self, 
                name="", 
                place="", 
                date="", 
                time="", 
                note="", 
                rounds=4
                ):
        self.name = name
        self.place = place
        self.date = date
        self.time = time
        self.note = note
        self.rounds = rounds
    
    def save_tournament(self):
        """ Methode servant à serialiser une instance de tournoi. """
        serialized_tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "time": self.time,
            "note": self.note,
            "rounds": self.rounds,
        }
        Tournament.tournament_db.insert(serialized_tournament)


