from field import Field

class Pawn:
    def __init__(self, belongsTo):
        self.belongsTo = belongsTo
        self.isOn = None

    def move(self, spaces):
        self.isOn.remove_pawn(self)
        for i in range(spaces):
            self.isOn = self.isOn.next
        self.isOn.add_pawn(self)

    def move_out(self):
        self.isOn = self.belongsTo.entry
        self.isOn.add_pawn(self)