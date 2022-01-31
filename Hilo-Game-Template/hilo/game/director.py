from game.dealer import Dealer
from game.player import Player

class Director:
    """A person who directs the game.
    
    The responsibility of the Director is to control the program event order.
    
    Attributes:
        playing (boolean): Whether or not the game is being played. 
    """


    def __init__(self):
        """Constructs a new Director instance. 
        
        Args:
            self (Director): an isntance of the Director.
        """
        self.playing = True
    
    def start_game(self):
        """Starts the main game loop.
        
        Args:
            self (Director): an isntance of the Director.
        """
        dealer = Dealer()
        player = Player()
        while self.playing:
            card1 = dealer.draw_card()
            player_guess = dealer.guess_draw()
            card2 = dealer.draw_card()
            player.update_points(card1, card2, player_guess)
            player.display_score()
            self.playing = dealer.replay()
            if self.playing:
                self.playing = player.check_points()


    

    
    
    
        