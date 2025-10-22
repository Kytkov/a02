class Intelligence:

    def __init__(self):
        self.name = 'CPU'
        self.score = 0

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('Score must be an integer')
        self.score = score
    
    def add_score(self, score):
        if not isinstance(score, int):
            raise ValueError('Score must be an integer')
        self.score += score

    def get_score(self):
        return self.score

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        self.name = name

    def get_name(self):
        return self.name

    def easy(self, temp_score):
       if temp_score>=5:
           self.add_score(temp_score)
       
       else:
        return

    def medium(self, temp_score, player_score):
        if temp_score>=15 and (player_score)-(self.score+temp_score)<30:
            self.add_score(temp_score)
            return 'done'
        
        elif temp_score>=20 and (player_score)-(self.score+temp_score)>=30:
            
            self.add_score(temp_score)
            return 'done' 
            
        else:
            return
    

    def hard(self, temp_score, player_score):
        if temp_score>=35 and (player_score-temp_score+player_score)>50:
            self.add_score(temp_score)
            return 'done'

        elif temp_score>=20 and (player_score)-(self.score+temp_score)>=30:
            self.add_score(temp_score)
            return 'done'
        
        else:
            return


    def set_difficulty(self, level):
        if not isinstance(level, str):
            return 'Incorrect input, Try again.'

        level = level.lower()
        if level == "easy":
            return self.easy()
        elif level == "medium":
            return self.medium()
        elif level == "hard":
            return self.hard()
        else:
            return 'Incorrect input, Try again.'