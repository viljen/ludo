from goal import Goal
from player import Player
from pawn import Pawn
from board import Board

class Field:
    def __init__(self, id: int, board: Board):
        self.id = id
        self.next = None
        self.goal = None
        self.pawns = []

    def add_pawn(self, pawn: Pawn) -> None:
        self.pawns.append(pawn)

    def remove_pawn(self, pawn: Pawn) -> None:
        self.pawns.remove(pawn)

    def pawn_count(self, player: Player) -> int:
        pawnCount = 0
        for pawn in self.pawns:
            if pawn.belongsTo == player:
                pawnCount += 1
        return pawnCount

    def blocked(self, activePlayer: Player) -> bool:
        # TODO: Blocked if occupied entry field
        try:
            return (len(self.pawns) >= 2) and pawns[0].belongsTo != activePlayer
        except IndexError:
            return False

    def fields_ahead(self, n: int) -> Field:
        # TODO: Fix movement involving goal areas
        field = self
        for i in range(n):
            field = field.next
        return field

    def __str__(self) -> str:
        # pawns_str = ", ".join([str(pawn) for pawn in self.pawns])
        return f"Field {self.id}"
