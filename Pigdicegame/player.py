"""Player class intended for the dice game."""


class Player:
    """
    Represents a player in the dice game.

    Attributes:
        name (str): The name of the player.
        score (int): The current score of the player.
    """

    def __init__(self, name):
        """
        Initialize a new player with a name and a starting score of 0.

        Args:
            name (str): The name of the player.

        Raises:
            ValueError: If name is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.name = name
        self.score = 0

    def set_score(self, score):
        """
        Set the player's score.

        Args:
            score (int): The score to set.

        Raises:
            ValueError: If score is not an integer.
        """
        if not isinstance(score, int):
            raise ValueError("Score must be an integer")
        self.score = score

    def add_score(self, score):
        """
        Add points to the player's current score.

        Args:
            score (int): The number of points to add.

        Raises:
            ValueError: If score is not an integer.
        """
        if not isinstance(score, int):
            raise ValueError("Score must be an integer")
        self.score += score

    def get_score(self):
        """
        Get the player's current score.

        Returns:
            int: The player's score.
        """
        return self.score

    def set_name(self, name):
        """
        Set the player's name.

        Args:
            name (str): The new name for the player.

        Raises:
            ValueError: If name is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.name = name

    def get_name(self):
        """
        Get the player's name.

        Returns:
            str: The player's name.
        """
        return self.name
