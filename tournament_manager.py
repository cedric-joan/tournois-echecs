from controllers.user_manager import check_date
from random import randint
from models.match import Match

RESULT_TO_FIND = randint(0, 2)
SEPARATOR = "-" * 60

class ControllerTournament:

    def input_controller_tournament():
        """ Methode servant a récupérer les saisies utilisteur."""
        print("\n")
        print(SEPARATOR)
        print("⚜  CREER UN TOURNOIS  ⚜")
        print(SEPARATOR)
        name = ControllerTournament.check_name()
        print(SEPARATOR)
        place = ControllerTournament.check_place()
        print(SEPARATOR)
        date_tournament = ControllerTournament.check_date_tournament()
        print(SEPARATOR)
        time = ControllerTournament.check_time()
        print(SEPARATOR)
        note = ControllerTournament.check_note()
        print(SEPARATOR)
        print(f"\nLe tournois {name.upper()} à {place.capitalize()} a été créé.")
        return [name.upper(), place.capitalize(), date_tournament, time, note]

    def check_name():  
        """ Methode servant a vérifier la saisie du nom."""
        name = input("\nNom : ")
        while len(name) < 3:
            name = input("Nom invalide: ")
            continue
        return name
                
    def check_place():
        """ Methode servant a vérifier la saisie du lieu."""
        place = input("\nLieu : ")
        while not place.isalpha() or len(place) < 3:
            place = input("Lieu invalide: ")
            continue
        return place

    def check_date_tournament():  
        """ Methode servant a vérifier la date."""
        date_tournament = input("\nDate \nFormat : jj/mm/aaaa : ")
        while not check_date(date_tournament):
            date_tournament = input("\nVeuillez saisir un format valide : jj/mm/aaaa : ")
            continue
        return date_tournament    

    def check_time():
        """ Methode servant a vérifier la saisie du temps."""
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
        return time
            
    def check_note():
        """ Methode servant a vérifier la saisie utilisateur."""
        note = input("\nAjoutez un commentaire ou appuyez sur entrée: ")
        if len(note) == 0:
            note = "Ancun commentaire"
        return note

class ControllerRound:

    def generate_match(player_a, player_b):
        """ Methode servant a générer un match."""
        print("\nDémarrez le match...")
        print(SEPARATOR)
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