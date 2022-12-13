

def  check_date(date):
        ok = True
        if len(date) != 8:
            ok = False
        if date.count("/") != 2:
            ok = False
        if date[2] != "/" or date[5] != "/":
            ok = False
        elif not (1 <= int(date[0:2]) <= 31) or not ( 1 <= int(date[3:5]) <= 12) or not int(date[6:]) > 0:
            ok = False
        return ok


def input_controller_player():
    SEPARATOR = "-" * 50

    last_name = input("\nNom : ")
    while not last_name.isalpha() or len(last_name) < 3:
        last_name = input("Nom invalide: ")
        continue
            
    print(SEPARATOR)

    first_name = input("\nPrenom : ")
    while not first_name.isalpha() or len(first_name) < 3:
        first_name = input("Prénom invalide: ")
        continue

    print(SEPARATOR)

    birthday = input("\nDate de naissance\nFormat : jj/mm/aa : ")
        
    while not check_date(birthday):
        birthday = input("\nVeuillez saisir un format valide : jj/mm/aa : ")
            
        
    print(SEPARATOR)
    genre = input("\nSexe\nf - Femme\nh - Homme\nVotre choix :")
    while genre not in ["f", "h"] :
        genre = input("Veuillez saisir f ou h : ")
        continue

    print(SEPARATOR)

    rank = input("\nClassement : ")
    while not rank.isdigit() or len(rank) < 1:
        rank = input("Veuillez saisir un chiffre")
        continue

    print("Le joueur a été créé")
            
    return last_name.upper(), first_name.capitalize(), birthday, genre, rank
