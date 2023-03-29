import random

class Die:
    def __init__(self):
        self.eyes = 6

    def roll(self):
        return random.randrange(1,self.eyes+1)