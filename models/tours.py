from dataclasses import dataclass

from models.player import Player

@dataclass
class Tours:
    nom: str
    date_debut: str
    heure_debut: str
    date_fin: str
    heure_fin: str

    def get_date_time():
        pass           


    

        