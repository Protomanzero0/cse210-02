from ast import Pass
from game.card import Card

class Dealer:
    """One who deals cards in a game, ensures rules are followed and game is played properly.
    
    The responsibility of Dealer is to handle player inputs, compare card values, and output results.
    
    Attributes:
        valid_input (Bool): Checks if player input is valid
        """
    def __init__(self):
        """Constructs a new Dealer instance.
        """
        Pass

    def get_draw(self):
        """Asks the user to guess if the next card drawn will be higher or lower.
        
        Args:
            self (Director): an isntance of the Director.
        """
        Pass

    def replay(self):
            """Asks the user if they'd like to play again after each round.
            
            Args:
                self (Director): an isntance of the Director.
            """
            Pass

    def do_output(self):
            """Displays the card drawn and current score.
            
            Args:
                self (Director): an isntance of the Director.
            """
            Pass

#Pull Request Testing