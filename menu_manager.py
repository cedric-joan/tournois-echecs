MENU_SCORE = """Choisissez parmi les 3 options suivantes:
0: Perdant
0,5: Match nul
1: Gagnant
Votre choix:  """

class MenuManager:

    def check_ids():
        """ Methode servant a identifier un joueur."""
        id = input("\nVeuillez saisir le rang: ")
        while not id.isdigit() or len(id) < 1:
            id = input("Veuillez saisir un chiffre: ")
            continue
        return int(id)

    def check_score():
        """ Methode servant a vérifier la saisie du score."""
        score = input(MENU_SCORE)
        while score not in ["0", "0.5", "1"] or score == "":
            score = input("\nVous n'avez pas saisi une valeur valide:  ")
            continue
        return float(score)           