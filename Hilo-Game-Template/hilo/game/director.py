from ast import Pass
from game.card import Card
from game.dealer import Dealer
from game.player import Player

dealer = Dealer
card = Card
player = Player

class Director:
    """
    A person who directs the game.
    
    The responsibility of the Director is to control the program event order.
    
    Attributes:
        playing (boolean): Whether or not the game is being played. 

    """

    def __init__(self):
        """
        Constructs a new Director instance. 
        
        Args:
            self (Director): an instance of the Director.
        """

        
        self.play = True
    
    def start_game(self):
        """
        Starts the main game loop.
        
        Args:
            self (Director): an instance of the Director.
        """
        card_val = card.draw(card)
        points = 300
        self.play == True

        while self.play == True and player.check_points(player, points) == True:
            print(f"The card is: {card_val}")
            guess = dealer.get_draw(dealer)
            next_card = card.draw(card)
            print(f"Next card was: {next_card}")
            points = player.do_update(player, guess, card_val, next_card, points)
            print(f"Your score is: {points}")
            self.play = dealer.replay(dealer)
            card_val = next_card
            print()


            


    

    
    
    
        