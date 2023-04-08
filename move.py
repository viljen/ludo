class Move:
    def __init__(self, start_field, end_field, active_pawn):
        self.start_field = start_field
        self.end_field = end_field
        self.active_pawn = active_pawn
        self.capture = False
        

    def execute():
        self.start_field.remove_pawn(self.active_pawn)
        if self.capture:
            for pawn in end_field.pawns:
                self.end_field.remove_pawn(pawn)
                pawn.isOn = None
        self.end_field.add_pawn(self.active_pawn)
        
    def capture():
        # Is it a capture move?
        for pawn in end_field.pawns:
            if (pawn.belongsTo is not active_pawn.belongsTo):
                return True
        return False
        
    def __str__(self):
        capture_str = ", with capture" if self.Capture else ""
        return f"Move from {start_field} to {end_field}{capture_str}."