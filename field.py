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

    def pawn_count(self, player):
        pawnCount = 0
        for pawn in self.pawns:
            if pawn.belongsTo == player:
                pawnCount += 1
        return pawnCount

    def __str__(self):
        pawns_str = ", ".join([str(pawn) for pawn in self.pawns])
        return f"Field {self.id}"
