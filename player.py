#from pawn import Pawn 
from entry import Entry 
from goal import Goal 
from strategy import Strategy 

class Player:
    def __init__(self, goal, entry, id):
        self.id = id
        self.strategy = Strategy()
        self.pawns = []
        self.goal = goal
        self.entry = entry
        self.goaled = 0

    def add_pawn(self, pawn):
        self.pawns.append(pawn)