from player import Player
from move import Move
from die import Die

from pawn import Pawn

class Turn:
    def __init__(self, player: Player):
        self.player = player
        self.die = Die()

    ###### Turn Rules ######

    ### Move rules
    # Each move rule returns a list of valid moves
    def get_moves(self) -> list[Move]:
        moves = []
        for pawn in self.player.pawns:
            if pawn.isOn == self.player.completed:
                pass
            elif pawn.isOn == self.player.pawnPool:
                moves += self.rule_move_out(pawn)
            elif pawn.isOn.goal != None:
                moves += self.rule_move_goal(pawn)
            else:
                moves += self.rule_move(pawn)
        return moves

    def rule_move_out(self, pawn: Pawn) -> list[Move]: 
        if self.die.eyes != 6:
            return []
        else:
            [Move(self.player.pawnPool, self.player.entry, pawn)]

    def rule_move(self, pawn: Pawn) -> list[Move]: 
        endField = pawn.isOn.fields_ahead(die.eyes)
        if endField.blocked(player):
            return []
        else:
            return [Move(pawn.isOn, endField, pawn)]

    def rule_move_goal(self, pawn: Pawn) -> list[Move]:
        # TODO: Implement
        pass

    ###### End of turn rules ######