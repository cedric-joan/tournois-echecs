from dataclasses import dataclass


SEPARATOR = "-" * 60

def  check_date(date):
        if len(date) != 10:
            return False
        elif date.count("/") != 2:
            return False
        if date[2] != "/" or date[5] != "/":
            return False
        if not date[0:2].isdigit() or not date[3:5].isdigit() or not date[6:].isdigit():
            return False
        elif not (1 <= int(date[0:2]) <= 31) or not ( 1 <= int(date[3:5]) <= 12) or not int(date[6:]) > 1900:
            return False
        return True


@dataclass
class ControllerPlayer:

    def check_last_name():    
        last_name = input("\nNom : ")
        while not last_name.isalpha() or len(last_name) < 3:
            last_name = input("Nom invalide: ")
            continue
        return last_name

    def check_first_name():            
        first_name = input("\nPrenom : ")
        while not first_name.isalpha() or len(first_name) < 3:
            first_name = input("Prénom invalide: ")
            continue
        return first_name

    def check_birthday():        
        birthday = input("\nDate de naissance\nFormat : jj/mm/aaaa : ")
        while not check_date(birthday):
            birthday = input("\nVeuillez saisir un format valide : jj/mm/aaaa : ")
            continue
        return birthday

    def check_genre():            
        genre = input("\nSexe\nf - Femme\nh - Homme\nVotre choix :")
        while genre not in ["f", "h"] :
            genre = input("Veuillez saisir f ou h : ")
            continue
        return genre

    def check_rank():        
        rank = input("\nClassement : ")
        while not rank.isdigit() or len(rank) < 1:
            rank = input("Veuillez saisir un chiffre")
            continue
        return rank

    def input_controller_player():
        print("\n")
        print(SEPARATOR)
        print("⚜  Ajouter un joueur  ⚜")
        print(SEPARATOR)
        last_name = ControllerPlayer.check_last_name()
        print(SEPARATOR)
        first_name = ControllerPlayer.check_first_name()
        print(SEPARATOR)
        birthday = ControllerPlayer.check_birthday()
        print(SEPARATOR)
        genre = ControllerPlayer.check_genre()
        print(SEPARATOR)
        rank = ControllerPlayer.check_rank()
        print(SEPARATOR)
        print(f"Le joueur {last_name.upper()} {first_name.capitalize()} a été créé")
        return [last_name.upper(), first_name.capitalize(), birthday, genre, rank]


                
