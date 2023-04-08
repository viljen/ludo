class Move:
    def __init__(self, start_field, end_field, active_pawn):
        self.start_field = start_field
        self.end_field = end_field
        self.active_pawn = active_pawn
        self.capture = False
        

    def execute():
        # Perform the move on the board
        self.start_field.remove_pawn(self.active_pawn)
        if self.capture:
            for pawn in end_field.pawns:
                self.end_field.remove_pawn(pawn)
                pawn.isOn = None
        self.end_field.add_pawn(self.active_pawn)

    # The following methods describe the properties of the move
        
    def capture():
        # Is it a capture move?
        for pawn in self.end_field.pawns:
            if (pawn.belongsTo is not self.active_pawn.belongsTo):
                return True
        return False

    def goalMove():
        # Is it a move within the goal area?
        return self.start_field.goal != None

    def intoGoal():
        # Does the move make the pawn enter the goal area?
        return (not self.goalMove()) and (self.end_field.goal != None)

    def createStack():
        # Does the move create a safe stack?
        for pawn in self.end_field.pawns:
            if (pawn.belongsTo is self.active_pawn.belongsTo):
                return True
        return False
    
    def breakStack():
        # Does the move break a safe stack?
        pawnCount = 0
        for pawn in self.start_field.pawns:
            if (pawn.belongsTo is self.active_pawn.belongsTo):
                pawnCount += 1
        return pawnCount == 2

    def endSafe():
        # Does the move end in safety?
        return self.createStack() or self.goalMove() or self.intoGoal()

    def startSafe():
        # Does the move start in safety?
        inStack = False

        
    def __str__(self):
        capture_str = ", with capture" if self.Capture else ""
        return f"Move from {start_field} to {end_field}{capture_str}."