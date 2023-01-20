
SEPARATOR = "-" * 60
MAX_PLAYERS_NUMBER = 8

class InputTournament:
    def __init__(self) -> None:
        pass

    def start_tournament(self):
        """ Methode servant a afficher les prérequis du tournois."""
        InputTournament.check_name(self)
        InputTournament.check_place(self)
        InputTournament.check_date_tournament(self)
        InputTournament.check_time(self)
        InputTournament.check_note(self)

    def display_start_tournament():    
        print("\n")
        print(SEPARATOR)
        print(f"⚜  POUR COMMENCER LE TOURNOI AJOUTEZ {MAX_PLAYERS_NUMBER} JOUEURS  ⚜")
        print(SEPARATOR)

    def check_name(self):  
        """ Methode servant a vérifier la saisie du nom."""
        print("\n")
        print(SEPARATOR)
        print("⚜  CREER UN TOURNOI  ⚜")
        print(SEPARATOR)
        self.name = input("\nNom  : ")

    def check_place(self):
        """ Methode servant a vérifier la saisie du lieu."""
        self.place = input("\nLieu : ")
        
    def check_date_tournament(self):  
        """ Methode servant a vérifier la date."""
        self.date = input("\nDate \nFormat : jj/mm/aaaa : ")

    def check_time(self):
        """ Methode servant a vérifier la saisie du temps."""
        self.time = ""
        while self.time not in ["1","2","3"]:
            self.time = input("\nContrôle de temps\n1 - Bullet\n2 - Blitz\n3 - Coup rapide\n\nVotre choix : ")
            if self.time == "1":
                self.time = "BULLET"
                break
            elif self.time == "2":
                self.time = "BLITZ" 
                break   
            elif self.time == "3":
                self.time = "COUP RAPIDE" 
                break 
            else:
                print("\nVous n'avez pas saisi une valeur valide.")    
            
    def check_note(self):
        """ Methode servant a vérifier la saisie utilisateur."""
        self.note = input("\nAjoutez un commentaire ou appuyez sur entrée: ")

    def create_round(self):
        """ Methode servant a saisir le nom du tour."""
        print("\n  Début du tour ")
        self.name = input("\n⚜  Saisissez le nom  ⚜ : ")

    def start_match():
        print("\nDémarrez le match...")
        print(SEPARATOR)

