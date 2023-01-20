# from models.player import Player
# from controllers.user_manager import UserManager

SEPARATOR = "-" * 60

MENU_SCORE = """Choisissez parmi les 3 options suivantes:
0: Perdant
0,5: Match nul
1: Gagnant
Votre choix:  """


class ViewsPlayers:
    def __init__(self) -> None:
        pass

    def print_name(self):    
        print(f"\nEntrez le score de {self}: ")  

    def input_player(self):
        ViewsPlayers.check_last_name(self)
        ViewsPlayers.check_first_name(self)
        ViewsPlayers.check_birthday(self)
        ViewsPlayers.check_genre(self)

    def check_last_name(self):            
        print(SEPARATOR)
        print("⚜  Ajouter un joueur  ⚜")
        self.last_name = input("\nNom : ")

    def check_first_name(self):            
        print(SEPARATOR)
        self.first_name = input("\nPrenom : ")

    def check_birthday(self):        
        print(SEPARATOR)
        self.birthday = input("\nDate de naissance\nFormat : jj/mm/aaaa : ")

    def check_genre(self):            
        print(SEPARATOR)
        self.genre = input("\nSexe\nf - Femme\nh - Homme\nVotre choix :")
        
    def check_rank():        
        print(SEPARATOR)
        rank = input("\nVeuillez saisir le numéro du classement : ")
        return rank 

    def check_ids():
        """ Methode servant a identifier un joueur."""
        id = input("\nVeuillez saisir le rang: ")
        return int(id)

    def check_score():
        """ Methode servant a vérifier la saisie du score."""
        score = input(MENU_SCORE)
        return float(score)    

MENU_JOUEUR = """Choisissez parmi les 4 options suivantes:
1 - Liste des joueurs par ordre alphabétique
2 - Ajouter un joueur
3 - Modification des classements
4 - Quitter
Votre choix:  """


class MenuPlayer:

    def display_players_menu():
        """ Methode servant a afficher le menu joueur."""
        print("\n")
        print(SEPARATOR)
        print(" ⚜   Menu Joueurs   ⚜ ")
        print(SEPARATOR)
        user_choice = ""
        while user_choice not in ["1","2","3","4"] or user_choice == " ":
            user_choice = input(MENU_JOUEUR)
            if user_choice == "1":
                # player.players_sorted_alphabetically()
                break
            elif user_choice == "2":
                # user_choice = UserManager.create_player()
                break
            elif user_choice == "3":
                # player.update_rank()
                break
            elif user_choice == "4":
                break  
            else :
                print("****Vous n'avez pas saisi le bon chiffre.****")

     


