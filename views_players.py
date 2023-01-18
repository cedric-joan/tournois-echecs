from dataclasses import dataclass

from models.player import Player

SEPARATOR = "-" * 60

MENU_JOUEUR = """Choisissez parmi les 4 options suivantes:
1 - Liste des joueurs par ordre alphabétique
2 - Ajouter un joueur
3 - Modification des classements
4 - Quitter
Votre choix:  """

@dataclass
class ViewsPlayers:

    def display_players_menu():
        """ Methode servant a afficher le menu joueur."""
        print("\n")
        print("-" * 30)
        print(" ⚜   Menu Joueurs   ⚜ ")
        print("-" * 30)
        user_choice = ""
        while user_choice not in ["1","2","3","4"] or user_choice == " ":
            user_choice = input(MENU_JOUEUR)
            if user_choice == "1":
                ViewsPlayers.players_sorted_alphabetically()
            elif user_choice == "2":
                user_choice = Player.create_player()
            elif user_choice == "3":
                Player.update_rank()
            elif user_choice == "4":
                break  
            else :
                print("****Vous n'avez pas saisi le bon chiffre.****")

    def players_sorted_alphabetically():
        """ Methode servant a trier les joueurs par ordre alphabétique.
        return : str nom des joueurs """
        db_all = Player.player_db.all()
        players = sorted(db_all, key=lambda player: player["last_name"], reverse=False)
        for player in players:
            print(player["last_name"])            