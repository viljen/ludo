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
        field = Field(0)
        self.fields.append(field)
        for i in range(51):
            field = Field(i+1)
            self.fields.append(field)
            self.fields[i].next = field

        self.fields[len(self.fields)-1].next = self.fields[0]

        #Initialize the players
        for i in range(4):
            entry = self.fields[i*13]
            field = Field(52+i)
            entry.goal = field
            goal = entry.goal
            player = Player(goal, entry, i) #Add goal and entry
            self.players.append(player)

            #Make goal area
            for j in range(5):
                next = Field(56+i)
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
            self.play_once(self.players[i])

    def play_once(self,player):
            num = self.die.roll()
            print(f"Player: {player.id}, roll: {num}")
            if num == self.die.eyes:
                print("Wheeee, move out")
                self.move_out(player, num)
                self.play_once(player)
            else:
                active = []
                for j in range(len(player.pawns)):
                    if player.pawns[j].isOn is not None:
                        active.append(player.pawns[j])

                #print(active)
                if len(active) > 0:
                    self.move(active, num)

    def move_out(self, player, die):
        moved_out = False
        for j in range(len(player.pawns)):
            if player.pawns[j].isOn is None:
                player.pawns[j].isOn = player.entry
                moved_out = True
                print("Wohoo")
                break
        if not moved_out:
            self.move(player.pawns, die)

    def move(self, pawns, die):
        print("Gibbigabb")
        for i in range(len(pawns)):
            if pawns[i] is not None:
                current = pawns[i].isOn
                for j in range(die):
                    current = current.next
                pawns[i].isOn = current
                break

    def print_board(self):
        text = ""
        for g in range(4):
            for i in range(13):
                text += "["
                for j in range(len(self.players)):
                    for k in range(len(self.players[j].pawns)):
                        if self.players[j].pawns[k].isOn is not None:
                            if self.players[j].pawns[k].isOn.id == i+g*13:
                                text += f"{j}"
                
                text += "]"
            text += "\n"
        
        print(text)

if __name__ == "__main__":
    b = Board()

    for i in range(10):
        b.play()

    b.print_board()