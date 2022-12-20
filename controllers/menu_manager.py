from dataclasses import dataclass

from controllers.tournament_manager import ControllerTournament
from views.views_players import ViewsPlayers
from views.views_tournament import ViewsTournament
from models.tournament import Tournament
# from views.views_main_menu import ViewsMainMenu

@dataclass
class MenuManager:

    def main_menu():
        user_choice = ""
        while user_choice not in ["1","2","3","4"] or user_choice == " ":
            user_choice = input("\n1 - Créer un nouveau tournoi\n2 - Menu joueurs\n3 - Menu tournois\n4 - Quitter\nVotre choix: ")
            if user_choice == "1":
                user_choice = ControllerTournament.input_controller_tournament()
                Tournament.create_tournament()
            elif user_choice == "2":
                user_choice = ViewsPlayers.display_players_menu()
            elif user_choice == "3":
                user_choice = ViewsTournament.display_tournament_menu()
                break
            elif user_choice == "4":
                print("     !!!!Au revoir!!!!.     ")
                break  
            else :
                print("****Vous n'avez pas saisi le bon chiffre.****")
        
    

                
    def player_menu():
        user_choice = ""
        while user_choice not in ["1","2","3","4"] or user_choice == " ":
            user_choice = input("\n1 - Liste des joueurs\n2 - Ajouter un joueur\n3 - Modifier le classement d'un joueur\n4 - Quitter\nVotre choix: ")
            if user_choice == "1":
                print("1")
                break
            elif user_choice == "2":
                print("2")
                break
            elif user_choice == "3":
                print("3")
                break
            elif user_choice == "4":
                # user_choice = ViewsMainMenu.main()
                break  
            else :
                print("****Vous n'avez pas saisi le bon chiffre.****")            