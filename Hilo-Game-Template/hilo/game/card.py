import random

class Card:
    """A typical playing card, numbered between 1 and 13.

    The responsibility of Card is to keep track of what card is drawn. 

    Attributes:
        value (int): The value of the card drawn, between 1 and 13.
    """



    def __init__(self):
        """Makes a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
    
    def draw(self):
        """Generates a new random value for the card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1,13)

    def display_card(self):
        '''This prints the value of the card'''
        print(f'The card is: {self.value}')