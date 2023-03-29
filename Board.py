from die import Die
from pawn import Pawn
from field import Field
from player import Player

class Board:
    die = Die()
    pawns = []
    players = []
    fields = []

    def __init__(self):
        #Put the fields on the board
        field = Field()
        self.fields.append(field)
        for i in range(55):
            field = Field()
            self.fields.append(field)
            self.fields[i].next = field

        self.fields[len(self.fields)-1].next = self.fields[0]

        #Initialize the players
        for i in range(4):
            player = Player(None, None) #Add goal and entry
            self.players.append(player)

        #Initialize the pawns
        gibb = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
        for i in range(16):
            pawn = Pawn(self.players[gibb[i]])
            self.pawns.append(pawn)
            self.players[gibb[i]].add_pawn(pawn)

    def play(self):
        for i in range(len(self.players)):
            num = self.die.roll()
            print(f"Player: {i}, roll: {num}")
            if num == 6:
                print("Wheeee, move out")
            else:
                active = []
                for j in range(len(self.players[i].pawns)):
                    if self.players[i].pawns[j].isOn is not None:
                        active.append(self.players[i].pawns[j])

                print(active)
                if len(active) > 0:
                    pass

    def move_out(self, player):
        pass

    def move(self, pawns):
        pass

if __name__ == "__main__":
    b = Board()

    for i in range(10):
        b.play()