from ast import Pass
from game.dealer import Dealer
dealer = Dealer

class Player:
    """
    One who plays the game.
    
    Responsibility: to handle card values and distribute points for guesses.
    
    Attributes:
        points (int): Number of player points
        can_play (bool): Whether or not a player can still play (only when points are higher than 0)
        
    """

    def __init__(self):
        """
        Constructs a new Player instance.
        """

        self.points = 300
        self.can_play = True

    def do_update(self, guess, card_val, next_card, points):
        """
        Updates the player's score.
        
        Args:
            self (Player): an instance of the Player.
        """

        if guess == "L" and card_val > next_card:
           points += 100
        elif guess == "H" and card_val < next_card:
            points += 100
        elif card_val == next_card:
            points += 0
        else:
            points -= 75
        
        return points
    
    def check_points(self, points):
        """
        Checks if player still has enough points to play.
        
        Args:
            self (Player): an instance of the Player.
        """
        
        if points > 0:
            can_play = True
        else:
            can_play = False

        return can_play