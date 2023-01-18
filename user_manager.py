SEPARATOR = "-" * 60

def  check_date(date):
        """ Methode servant a vérifier la date."""
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

def check_name(name):    
    while not name.isalpha() or len(name) < 3:
        name = input("Saisie invalide: ")
        continue
    return name

class ControllerPlayer:

    def check_last_name():            
        last_name = input("\nNom : ")
        return check_name(last_name)    

    def check_first_name():            
        first_name = input("\nPrenom : ")
        return check_name(first_name)

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
        rank = input("\nVeuillez saisir le numéro du classement : ")
        while not rank.isdigit() or len(rank) < 1:
            rank = input("Veuillez saisir un chiffre")
            continue
        return rank

    def input_controller_player():
        """ Methode servant a récupérer les saisies utilisteur."""
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
        rank = "0"
        print(SEPARATOR)
        score = 0.0
        print(f"Le joueur {last_name.upper()} {first_name.capitalize()} a été créé")
        print("\n")
        return [last_name.upper(), first_name.capitalize(), birthday, genre, rank, score] 