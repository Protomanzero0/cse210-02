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
        self.run_game = True

    def guess_draw(self):
        """Asks the user to guess if the next card drawn will be higher or lower.
        
        Args:
            self (dealer): an instance of the Dealer.
        """
        users_guess = input("Higher or Lower [h/l]: ")
        return users_guess.lower()


    def replay(self):
            """Asks the user if they'd like to play again after each round.
            
            Args:
                self (dealer): an instance of the Dealer.
            """
            play_again = input("Do you want to play again (y/n): ")
            if play_again == "n":
                self.run_game = False
            return self.run_game


    def draw_card(self):
            """Displays the card drawn and current score.
            
            Args:
                self (dealer): an instance of the Dealer.
            """
            card = Card()
            card.draw()
            card.display_card()
            return card.value

