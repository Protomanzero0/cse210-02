from ast import Pass
from game.dealer import Dealer

class Player:
    """One who plays the game.
    
    Responsibility: to handle card values and distribute points for guesses.
    
    Attributes:
        points (int): Number of player points
        can_play (bool): Whether or not a player can still play (only when points are higher than 0)
        
    """
    def __init__(self):
        """Constructs a new Player instance.
        """
        points = 300
        can_play = True

    def do_update(self):
        """Updates the player's score.
        
        Args:
            self (Director): an instance of the Director.
        """
        Pass
    
    def check_points(self, points):
        """Checks if player still has enough points to play."""
        Pass