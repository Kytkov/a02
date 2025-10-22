"""player class intended for the dice game."""


class Player:
    """player class intended for the dice game."""

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.name = name
        self.score = 0

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("Score must be an integer")
        self.score = score

    def add_score(self, score):
        if not isinstance(score, int):
            raise ValueError("Score must be an integer")
        self.score += score

    def get_score(self):
        return self.score

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.name = name

    def get_name(self):
        return self.name
