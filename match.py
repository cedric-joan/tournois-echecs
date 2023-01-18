class Match:
    """ Classe servant a créer une instance de match."""
    def __init__(self, player_a, player_b, score_a, score_b):
        self.player_a = player_a
        self.player_b = player_b
        self.score_a = score_a
        self.score_b = score_b

    def list_pairs(player_a, score_a, player_b, score_b):
        """ Methode servant a créer une paire de joueur."""
        list_player_a = []
        list_player_b = []
        tuple_pairs = ()
        list_player_a = player_a, score_a
        list_player_b = player_b, score_b
        tuple_pairs = list_player_a, list_player_b
        return tuple_pairs