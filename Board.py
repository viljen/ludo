from die import Die
from pawn import Pawn
from field import Field
from player import Player

class Board:
    def __init__(self):
        self.die = Die()
        self.pawns = []
        self.players = []
        self.fields = []

        #Put the fields on the board
        field = Field()
        self.fields.append(field)
        for i in range(51):
            field = Field()
            self.fields.append(field)
            self.fields[i].next = field

        self.fields[len(self.fields)-1].next = self.fields[0]

        #Initialize the players
        for i in range(4):
            entry = self.fields[i*13]
            field = Field()
            entry.goal = field
            goal = entry.goal
            player = Player(goal, entry) #Add goal and entry
            self.players.append(player)

            #Make goal area
            for j in range(5):
                next = Field()
                goal.next = next
                goal = next

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
            if num == self.die.eyes:
                print("Wheeee, move out")
                self.move_out(self.players[i])
            else:
                active = []
                for j in range(len(self.players[i].pawns)):
                    if self.players[i].pawns[j].isOn is not None:
                        active.append(self.players[i].pawns[j])

                #print(active)
                if len(active) > 0:
                    self.move(self.players[i].pawns)

    def move_out(self, player):
        moved_out = False
        for j in range(len(player.pawns)):
            print(player.pawns[j].isOn)
            if player.pawns[j].isOn is None:
                player.pawns[j].isOn = player.entry
                print(player.pawns[j].isOn)
                moved_out = True
                print("Wohoo")
                break
        if not moved_out:
            self.move(player.pawns)

    def move(self, pawns):
        print("Gibbigabb")

if __name__ == "__main__":
    b = Board()

    for i in range(10):
        b.play()