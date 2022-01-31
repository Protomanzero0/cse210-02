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
        self.points = 300
        self.can_play = True

    def display_score(self):
        """Display the player's score.
        
        Args:
            self (player): an instance of the Player.
        """
        print(f'Your score is: {self.points}')
    
    def check_points(self):
        """Checks if player still has enough points to play."""
        if self.points <= 0:
            self.can_play = False
            print('You do not have enough points to play again.')
        return self.can_play

    def update_points(self, card1, card2, guess):
        '''Update the player's score.'''
        if card1 > card2 and guess == 'l':
            self.points += 100
        if card1 < card2 and guess == 'h':
            self.points += 100
        if card1 > card2 and guess == 'h':
            self.points -= 75
        if card1 < card2 and guess == 'l':
            self.points -= 75
        if card1 == card2:
            pass
        return self.points
