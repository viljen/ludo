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

    def __str__(self):
        pawns_str = ", ".join([str(pawn) for pawn in self.pawns])
        return f"Field {self.id}, containing pawns: {pawns_str}"
