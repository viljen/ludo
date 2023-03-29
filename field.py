from goal import Goal 

class Field:
    def __init__(self, id):
        self.id = id
        self.next = None
        self.goal = None
        self.pawns = []

    def add_pawn(self, pawn):
        self.pawns.append(pawn)

    def remove_pawn(self, pawn):
        self.pawns.remove(pawn)
