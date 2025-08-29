import random

class Dice:
    def __init__(self):
       
        self.values = [0, 0]
    
    def roll(self):
        self.values[0] = random.randint(1, 6)
        self.values[1] = random.randint(1, 6)
        return tuple(self.values)
    
    def get_values(self):
        return tuple(self.values)
    
    def is_doubles(self):
        return self.values[0] == self.values[1]