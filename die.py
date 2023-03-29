import random

class Die:
    eyes = 6

    def roll(self):
        return random.randrange(1,self.eyes)