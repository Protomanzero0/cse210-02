from ast import Pass
from game.card import Card
card = Card

class Dealer:
    """One who deals cards in a game, ensures rules are followed and game is played properly.
    
    The responsibility of Dealer is to handle player inputs, compare card values, and output results.
    
    Attributes:
        valid_input (Bool): Checks if player input is valid
        """

    def __init__(self):
        """Constructs a new Dealer instance.
        """

        self.users_guess = ""
        self.play_again = ""
        self.run_game = True

    def get_draw(self):
        """Asks the user to guess if the next card drawn will be higher or lower.
        
        Args:
            self (Director): an isntance of the Director.
        """
        self.users_guess = input("Higher or Lower? (H/L): ")
        return self.users_guess


    def replay(self):
            """Asks the user if they'd like to play again after each round.
            
            Args:
                self (Director): an isntance of the Director.
            """
            run_game = True
            self.play_again = input("Do you want to play again (y/n): ")
            if self.play_again != "y":
                run_game = False
            return run_game


    # def do_output(self):
    #         """Displays the card drawn and current score.
            
    #         Args:
    #             self (Director): an isntance of the Director.
    #         """
    #         Pass

