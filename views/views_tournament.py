from models.player import Player

SEPARATOR = "-" * 60
MAX_PLAYERS_NUMBER = 8

class ViewsTournament:

    def start_tournament():
        """ Methode servant a afficher les prérequis du tournois."""
        print("\n")
        print(SEPARATOR)
        print(f"⚜  POUR COMMENCER LE TOURNOIS AJOUTER {MAX_PLAYERS_NUMBER} JOUEURS  ⚜")
        print(SEPARATOR)
        Player.create_list_players()    
    
    def create_round():
        """ Methode servant a saisirle nom du tournois."""
        print("\n")
        print("  Début du tour ")
        name = input("\n⚜  Saisissez le nom  ⚜ : ")
        return name  