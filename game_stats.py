class GameStats:
    """Class responsible for keeping track of game statistics."""
    def __init__(self):
        """Initialization of the class."""
        self.reset_stats()

    def reset_stats(self):
        """Resets the game statistics when the program starts."""
        self.p1_score = 0
        self.p2_score = 0
