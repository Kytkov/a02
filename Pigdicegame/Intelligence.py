class Intelligence:
    """The game logic for the computer"""

    def __init__(self):
        self.name = 'CPU'
        self.score = 0
        self.difficulty = NotImplemented

    def set_score(self, score):
        """set computer's score"""
        if not isinstance(score, int):
            raise ValueError('Score must be an integer')
        self.score = score
    
    def add_score(self, score):
        """add computer's score"""
        if not isinstance(score, int):
            raise ValueError('Score must be an integer')
        self.score += score
    
    def get_score(self):
        """return computer's score"""
        return self.score

    def set_name(self, name):
        """set computer's name"""
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        self.name = name

    def get_name(self):
        """return computer's name"""
        return self.name

    def easy(self, temp_score):
       """check if computer should roll or stay"""
       if temp_score>=20:
          return True 
       
       return False

    def medium(self, temp_score, player_score):
        """check if computer should roll or stay"""
        if temp_score>=15 and (player_score)-(self.score+temp_score)<10:
            
            return True
        
        
        # elif temp_score>=20 and (player_score)-(self.score+temp_score)>=30:
            
        #     self.add_score(temp_score)
        #     return 'done' 
            
        else:
            return False
    

    def hard(self, temp_score, player_score):
        """check if computer should roll or stay"""
        #if temp_score>=35 and (player_score-temp_score+player_score)>50:
        #    self.add_score(temp_score)
        #   return True
        if temp_score>=5 or (player_score)-(self.score+temp_score)>=10:
            return True
        
        else:
            return False


    def set_difficulty(self, level):
        if not isinstance(level, str):
            return 'Incorrect input, Try again.'

        level = level.lower()

        if level == "e":
            self.difficulty = "easy"
        elif level == "m":
            self.difficulty = "medium"
        elif level == "h":
            self.difficulty = "hard"
        else:
            return 'Incorrect input, Try again.'
        

        # level = level.lower()
        # if level == "easy":
        #     return self.easy()
        # elif level == "medium":
        #     return self.medium()
        # elif level == "hard":
        #     return self.hard()
        # else:
        #     return 'Incorrect input, Try again.'

    def make_choice(self, temp_score, player_score):
    
        if self.difficulty == "easy":
           return self.easy(temp_score)
        elif self.difficulty == "medium":
            return self.medium(temp_score, player_score)
        else:
            return self.hard(temp_score,player_score)