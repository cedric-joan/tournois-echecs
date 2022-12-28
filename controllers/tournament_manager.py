from dataclasses import dataclass
from controllers.user_manager import check_date
from random import randint

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

        date = input("\nDate \nFormat : jj/mm/aaaa : ")
        while not check_date(date):
            date = input("\nVeuillez saisir un format valide : jj/mm/aaaa : ")

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
           
        print(SEPARATOR)
            
        print(f"\nLe tournois {name.upper()} à {place.capitalize()} a été créé.")
        return [name.upper(), place.capitalize(), date, time, note]


WIN = 2
LOSS = 1

SKIP_TURN = False
RESULT_TO_FIND = randint(1, 2)

LAST_NAME = "joan"
FIRST_NAME = "éric"

@dataclass
class ControllerRound:

    def random_result(players):
            print("\nDémarrez le match...")
            input("\nAppuyez sur Entrée ! ")
            
            if RESULT_TO_FIND == WIN:
                print(f" Le joueur {LAST_NAME} {players} a gagné")
            elif RESULT_TO_FIND == LOSS:
                print(f" Le joueur {FIRST_NAME} {players} a perdu")
            else: 
                print("fin du jeu")
            return
