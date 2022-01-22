import random

class Card:
    """A card that can have a value between 1 and 13.

    The responsibility of card is to keep track of the number that represent it and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of the card.
        points (int): The number of points the card is worth.
    """

    def __init__( self ):
        """Constructs a new instance of Card with a value and points attribute.

        Args:
            self ( Card ): An instance of Card.
        """
        self.value = 0

    def mix( self ):
        """Generates a new random value and calculates the points.
        
        Args:
            self ( Card ): An instance of Card.
            answer : The answer from user, to compare with the value of the card.
        """
        self.value = random.randint( 1, 13 )