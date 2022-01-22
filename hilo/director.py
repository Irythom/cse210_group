from card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        curren_card: The card that is current displayed.
        next_card: The next card to be displayed
        is_playing (boolean): Whether or not the game is being played.
        is higher (boolean): The choose of the player for the higher or lower option.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        current_card = Card()
        next_card = Card()
        self.current_card = current_card
        self.next_card = next_card
        self.is_playing = True
        self.is_higher = False
        self.score = 300
        self.total_score = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.keep_playing()
        
        print( "Thank you for playing!" )

    def get_inputs( self ):
        """Ask the user for the guess of the next card.

        Args:
            self ( Director ): An instance of Director.
        """
        if self.current_card.value == 0:
            self.current_card.mix()
        if self.next_card.value == 0:
            self.next_card.mix()
        if self.current_card.value == self.next_card.value:
            self.next_card.mix()

        print( f"\nThe card is: {self.current_card.value}" )
        next_card = input( "Higher or lower? [h/l] " )
        self.is_higher = ( next_card.lower() == "h" )
       
    def do_updates( self ):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if self.is_higher:
            if self.current_card.value < self.next_card.value:
                self.score += 100
            else:
                self.score -= 75
        else:
            if self.current_card.value > self.next_card.value: 
                self.score += 100
            else: self.score -= 75
        
        self.total_score = self.score             

    def do_outputs(self):
        """Displays the card and the score. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print( f"Next card was: {self.next_card.value}" )
        print(f"Your score is: {self.total_score}")
        self.is_playing == (self.score > 0)

    def keep_playing( self ):
        """Ask the user if they want to play again.

        Args:
            self ( Director ): An instance of Director.
        """
        keep_playing = input( "Play again? [y/n] " )
        self.is_playing = ( keep_playing == "y" )
        self.current_card.value = self.next_card.value