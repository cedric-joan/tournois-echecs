from dataclasses import dataclass
from controllers.user_manager import check_date


SEPARATOR = "-" * 60

@dataclass
class ControllerTournament:

    def input_controller_tournament():

        print("\n")
        print(SEPARATOR)
        print("⚜  CREER UN TOURNOIS  ⚜")
        print(SEPARATOR)

        name = input("\nNom : ")
        while not name.isalpha() or len(name) < 3:
            name = input("Nom invalide: ")
            continue
                
        print(SEPARATOR)

        place = input("\nLieu : ")
        while not place.isalpha() or len(place) < 3:
            place = input("Lieu invalide: ")
            continue

        print(SEPARATOR)

        date_now = input("\nDate \nFormat : jj/mm/aaaa : ")
        while not check_date(date_now):
            date_now = input("\nVeuillez saisir un format valide : jj/mm/aaaa : ")

        print(SEPARATOR)

        time = ""
        while time not in ["1","2","3"]:
            time = input("\nContrôle de temps\n1 - Bullet\n2 - Blitz\n3 - Coup rapide\n\nVotre choix : ")
            if time == "1":
                time = "BULLET"
                break
            elif time == "2":
                time = "BLITZ" 
                break   
            elif time == "3":
                time = "COUP RAPIDE" 
                break 
            else:
                print("\nVous n'avez pas saisi une valeur valide.")    
            
        print(SEPARATOR)

        note = input("\nAjoutez un commentaire ou appuyez sur entrée: ")
        if len(note) == 0:
            note = "Ancun commentaire"
        else:
            return note    
        print(SEPARATOR)
            
        print(f"\nLe tournois {name.upper()} à {place.capitalize()} a été créé.")
        return name.upper(), place.capitalize(), date_now, time, note

    