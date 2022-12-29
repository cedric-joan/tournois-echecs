from dataclasses import dataclass
from controllers.user_manager import check_date
from models.match import Match

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

MENU_SCORE = """Choisissez parmi les 3 options suivantes:
0: Perdant
0,5: Match nul
1: Gagnant
Votre choix:  """

RESULT_TO_FIND = randint(0, 2)

@dataclass
class ControllerRound:

    def random_result(player_a,score_a, player_b, score_b):
        print("\nDémarrez le match...")
        print(SEPARATOR)

        winner = 2
        loser = 1
        if RESULT_TO_FIND == winner:
            ControllerRound.print_result_and_score_a(player_a=player_a, player_b=player_b)
            score_a = ControllerRound.check_score(score_a)
            print(f"\nEntrez le score de {player_b}: ")
            score_b = ControllerRound.check_score(score_b)
            result = Match.list_pair(player_a=player_a, score_a=score_a, player_b=player_b, score_b=score_b)
            print("fin du match")
            return result
        elif RESULT_TO_FIND == loser:
            ControllerRound.print_result_and_score_b(player_a=player_a, player_b=player_b)
            score_a = ControllerRound.check_score(score_b)
            print(f"\nEntrez le score de {player_a}: ")
            score_b = ControllerRound.check_score(score_a)
            result = Match.list_pair(player_a=player_a, score_a=score_a, player_b=player_b, score_b=score_b)
            print("fin du match")
            return result
        else:
            ControllerRound.print_result_and_score_nul(player_a=player_a, player_b=player_b)
            score_a = ControllerRound.check_score(score_a)
            print(f"\nEntrez le score de {player_b}: ")
            score_b = ControllerRound.check_score(score_b)
            result = Match.list_pair(player_a=player_a, score_a=score_a, player_b=player_b, score_b=score_b)
            print("fin du match")
            return result

    def check_score(score):
        print("\n")
        score = input(MENU_SCORE)
        while score not in ["0","0,5","1"]:
            score = input("\nVous n'avez pas saisi une valeur valide:  ")
            continue
        return score


    def print_result_and_score_a(player_a, player_b):
        print(f" Le joueur {player_a} a gagné \n Le joueur {player_b} a perdu")
        print(f"\nEntrez le score de {player_a}: ")

    def print_result_and_score_b(player_a, player_b):
        print(f" Le joueur {player_b} a gagné \n Le joueur {player_a} a perdu")
        print(f"\nEntrez le score de {player_b}: ")

    def print_result_and_score_nul(player_a, player_b):
        print(f" Les joueurs {player_a} et {player_b} ont fait match nul")
        print(f"\nEntrez le score de {player_a}: ")    
