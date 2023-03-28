from field import Field

class Pawn:
    def __init__(self, belongsTo):
        self.belongsTo = belongsTo
        self.isOn = None