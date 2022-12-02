from dataclasses import dataclass


@dataclass
class Tournoi:
       def __init__(self, nom="", lieu="", date="", nb_tours=4, joueurs=[], temps="", note=""):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nb_tours = nb_tours
        self.joueurs = joueurs
        self.temps = temps
        self.note = note

@dataclass
class Joueur:
    nom :str
    prenom :str
    date_de_naissance :str
    sexe :str
    classement :str

    def create_player():
        separator = "-" * 50
        print(separator)
        nom = input("\nNom : ")
        while nom.isdigit():
            nom = input("\nNom : ")
            if nom.isdigit():
                print("Veuillez saisir des lettres")
                    
        print(separator)
        prenom = input("\nPrenom : ")
        while prenom.isdigit():
            prenom = input("\nPrenom : ")
            if prenom.isdigit():
                print("Veuillez saisir des lettres")

        print(separator)
        date_de_naissance = ""
        while not date_de_naissance.isdigit():
            date_de_naissance = input("\nDate de naissance\nFormat : jj/mm/aaaa : ")
            if not date_de_naissance.isdigit():
                print("Veuillez saisir des chiffres")
            
        print(separator)
        sexe_choix = ""
        while not sexe_choix.isdigit() :
            sexe_choix = input("\nSexe\n1 - Femme\n2 - Homme\n3 - Autre\n\nVotre choix : ")
            if not sexe_choix.isdigit():
                print("Veuillez saisir un chiffre")
            while int(sexe_choix) > 3 :
                sexe_choix = input("\nSexe\n1 - Femme\n2 - Homme\n3 - Autre\n\nVotre choix : ")
                if int(sexe_choix) > 3 :
                    print("Veuillez saisir un chiffre de 1 à 3")

        print(separator)
        classement = input("\nClassement : ")
        while not classement.isdigit():
            classement = input("\nClassement : ")
            if not classement.isdigit():
                print("Veuillez saisir un chiffre")
                print(separator)
        return nom,prenom,date_de_naissance,sexe_choix,classement
            

    def list_players():
        users = []
        for _ in range(2):
            user = Joueur.create_player()
            users.append(user)
        return users    


if __name__ == "__main__":
    users = Joueur.list_players()
    # user = Joueur.create_player()
    # print(user)
    print(users)

