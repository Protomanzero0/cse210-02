from game.card import Card


class Director:
    """A person who directs the game.
    
    The responsibility of the Director is to control the program event order.
    
    Attributes:
        card (int): A single Card instance.
        playing (boolean): Whether or not the game is being played. 
        score (int): The score for one round of the game.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director instance. 
        
        Args:
            self (Director): an isntance of the Director.
        """

        self.card = 0
        self.playing = True
        self.score = 0
        self.total_score = 0

        card = Card()

    def start_game(self):
        """Starts the main game loop.
        
        Args:
            self (Director): an isntance of the Director.
        """
        while self.playing:
            self.get_draw()
            self.replay()
            self.do_update()
            self.do_output()

    def get_draw(self):
        """Asks the user to guess if the next card drawn will be higher or lower.
        
        Args:
            self (Director): an isntance of the Director.
        """

    def replay(self):
        """Asks the user if they'd like to play again after each round.
        
        Args:
            self (Director): an isntance of the Director.
        """
    def do_update(self):
        """Updates the player's score.
        
        Args:
            self (Director): an isntance of the Director.
        """
    def do_output(self):
        """Displays the card drawn and current score.
        
        Args:
            self (Director): an isntance of the Director.
        """
        