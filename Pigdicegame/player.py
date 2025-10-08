class player:
    
    def __init__(self, name):
        self.name = name
    
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


