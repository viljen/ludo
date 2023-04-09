from field import Field
from pawn import Pawn

class Move:
    def __init__(self, startField: Field, endField: Field, activePawn: Pawn):
        self.startField = startField
        self.endField = endField
        self.activePawn = activePawn
        self.player = activePawn.belongsTo

    def execute(self) -> None:
        # Perform the move on the board
        self.startField.remove_pawn(self.activePawn)
        if self.capture():
            for pawn in endField.pawns:
                self.endField.remove_pawn(pawn)
                pawn.isOn = None
        self.endField.add_pawn(self.activePawn)

    ###### Move Properties ######
    # The following methods describe the properties of the move
    def capture(self) -> bool:
        # Is it a capture move?
        for pawn in self.endField.pawns:
            if (pawn.belongsTo is not self.player):
                return True
        return False

    def goal_move(self) -> bool:
        # Is it a move within the goal area?
        return self.startField.goal != None

    def into_goal(self) -> bool:
        # Does the move make the pawn enter the goal area?
        return (not self.goalMove()) and (self.endField.goal != None)

    def create_stack(self) -> bool:
        # Does the move create a safe stack?
        pawnCount = self.endField.count_pawns(self.player) 
        return pawnCount >= 1
    
    def break_stack(self) -> bool:
        # Does the move break a safe stack?
        pawnCount = self.startField.count_pawns(self.player)
        return pawnCount == 2

    def end_safe(self) -> bool:
        # Does the move end in safety?
        return self.createStack() or self.goalMove() or self.intoGoal()

    def start_safe(self) -> bool:
        # Does the move start in safety?
        pawnCount = self.startField.count_pawns(self.player)
        return pawnCount >= 2 or self.goal_move() or self.startField == self.player.entry

    ###### End Move Properties ######

    def __str__(self) -> str:
        return f"Move from {startField} to {endField}"