from views.views_players import ViewsPlayers, MenuPlayer
from views.views_tournament import InputTournament
from models.tournament import Tournament
from models.rounds import Rounds
from controllers.user_manager import UserManager

SEPARATOR = "-" * 60

class ViewsMainMenu:
    def __init__(self, views) -> None:
        self.views = views


    def main():
        """ Methode servant a afficher le menu principal."""
        print("\n")
        print("-" * 30)
        print("Menu principal: ")
        print("-" * 30)
        views_tournament = InputTournament()
        views_players = MenuPlayer()
        user_choice = ""
        while user_choice not in ["1","2","3","4"] or user_choice == " ":
            user_choice = input("\n1 - Créer un nouveau tournoi\n2 - Menu joueurs\n3 - Menu tournois\n4 - Quitter\nVotre choix: ")
            if user_choice == "1":
                views_tournament.start_tournament()
                views_tournament.display_start_tournament()
                UserManager.create_list_players()
                Rounds.save_round()
                Rounds.next_round()
            elif user_choice == "2":
                user_choice = views_players.display_players_menu()
            elif user_choice == "3":
                user_choice = ViewsTournaments.display_tournament_menu()
            elif user_choice == "4":
                print("\n")
                print("-" * 30)
                print("   ⚜⚜   Au revoir   ⚜⚜  ")
                print("-" * 30)
                break
            else :
                print("****Vous n'avez pas saisi le bon chiffre.****")


MENU_USER = """Choisissez parmi les 6 options suivantes:
            1 - Liste de tous les tournois,
            2 - Liste des joueurs d'un tournoi,
            3 - Nom et dates d'un tournois,
            4 - Liste de tous les tours d'un tournoi,
            5 - Liste de tous les matchs d'un tournoi,
            6 - Revenir au menu précédent
Votre choix:  """            
        
class ViewsTournaments:

    def display_tournament_menu():
        """ Methode servant a afficher le menu tournoi."""
        print("\n")
        print("-" * 30)
        print("Menu Tournois: ")
        print("-" * 30)
        user_choice = ""
        while user_choice not in ["1","2","3","4","5","6"] or user_choice == " ":
            user_choice = input(MENU_USER)
            if user_choice == "1":
                ViewsTournaments.list_tournaments()
                break
            elif user_choice == "2":
                ViewsTournaments.display_players_by_match()
                break
            elif user_choice == "3":
                ViewsTournaments.search_tournament()
                break
            elif user_choice == "4":
                ViewsTournaments.list_rounds()
                break  
            elif user_choice == "5":
                ViewsTournaments.list_matches()
                break
            elif user_choice == "6":
                break
            else :
                print("****Vous n'avez pas saisi le bon chiffre.****")

    def list_rounds():
        """ Methode servant a afficher la liste des tours."""
        list_rounds = Rounds.rounds_db.all()
        for round in list_rounds:
            round_start = round["start"]
            round_end = round["end"]
            round_list = round["list_match"]
            print(round["round_name"])
            print(f"Début du tour: {round_start}")
            print(f"listes des matchs: {round_list}")
            print(f"Fin du tour: {round_end}")
            print("\n")

    def display_players_by_match():
        """ Methode servant a afficher la list des joueurs d'un tournois."""
        display_list_players = Rounds.list_players_by_match()
        print(display_list_players)       

    def list_matches():
        """ Methode servant a afficher la list de tous les matchs."""
        list_matches = Rounds.rounds_db.all()
        for i, match in enumerate(list_matches,1):
            match_list = match["list_match"]
            print(f"listes des matchs {i}: {match_list}")
            print("\n")   

    def search_tournament():
        """ Methode servant a rechercher un tournois."""
        tournament = Tournament.tournament_db.all()
        name_tournament = tournament[0]["name"]
        date_tournament = tournament[0]["date"]
        print("\n")   
        name = input("Saisissez le nom du tournois en lettre capitale: ")
        date = input("Saisissez la date : ")
        if name == name_tournament and date == date_tournament:
            print(tournament)
        else:
            print("\nVous n'avez pas saisi une valeur valide:  ")    

    def list_tournaments():
        """ Methode servant a afficher la Liste de tous les tournois."""
        list_tournaments = Tournament.tournament_db.all()
        print(list_tournaments)    