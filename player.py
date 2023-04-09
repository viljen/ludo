# TODO: Create start field self.pawnPool, not None
# TODO: Create field for completed pawns, self.completed
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

    def __str__(self):
        return f"Player {self.id}"