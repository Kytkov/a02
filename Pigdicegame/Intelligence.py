class Intelligence:

    def __init__(self):
        self.name = "CPU"
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

    def easy(self):
        pass

    def medium(self):
        pass

    def hard(self):
        pass

    def set_difficulty(self, level):
        if not isinstance(level, str):
            return "Incorrect input, Try again."

        level = level.lower()
        if level == "easy":
            return self.easy()
        elif level == "medium":
            return self.medium()
        elif level == "hard":
            return self.hard()
        else:
            return "Incorrect input, Try again."
