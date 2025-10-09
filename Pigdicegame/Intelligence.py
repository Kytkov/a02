class Intelligence:

    def __init__(self):
        self.name = 'CPU'

    def set_score(self, score):
        self.score = score

    def add_score(self, score):
        self.score =+ score

    def get_score(self):
        return self.score
    
    def set_name(self, name):
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
        
        if level.lower() == "easy":
            self.easy()
        elif level.lower() == "medium":
            self.medium
        elif level.lower() == "hard":
            self.hard
        else:
            print('Incorrect input, Try again.') 


