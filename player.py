#from pawn import Pawn 
from entry import Entry 
from goal import Goal 
from strategy import Strategy 

class Player:
    strategy = Strategy()
    pawns = []

    def __init__(self, goal, entry):
        self.goal = goal
        self.entry = entry

    def add_pawn(self, pawn):
        self.pawns.append(pawn)