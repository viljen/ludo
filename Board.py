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

                if len(active) > 0:
                    self.move(active, num)

    def move_out(self, player, die):
        moved_out = False
        for j in range(len(player.pawns)):
            if player.pawns[j].isOn is None:
                player.pawns[j].move_out()
                moved_out = True
                print("Wohoo")
                break
        if not moved_out:
            self.move(player.pawns, die)

        self.print_board()
        input()

    def move(self, pawns, die):
        print("Gibbigabb")
        for i in range(len(pawns)):
            if pawns[i] is not None:
                pawns[i].move(die)
                break

        self.print_board()
        input()

    def print_board(self):
        """
        text = ""
        for g in range(4):
            text += "\n"
            for i in range(13):
                text += "["
                if len(self.fields[i+g*13].pawns) > 0:
                    for pawn in self.fields[i+g*13].pawns:
                        text += str(pawn.belongsTo.id)   
                else:
                    text += " "       
                text += "]"
        print(text+"\n")
        """
        i = 49
        j = 48
        text = "                  "
        for g in range(3):
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i += 1
            text += "]"  

        i = 0
        text += "\n"
        for g in range(5):
            text += "                  ["
            if len(self.fields[j].pawns) > 0:
                    for pawn in self.fields[j].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            j -= 1
            text += "]   " 
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i += 1
            text += "]\n" 

        j -= 5
        for g in range(6):
            text += "["
            if len(self.fields[j].pawns) > 0:
                    for pawn in self.fields[j].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            j += 1
            text += "]"

        text += "         "
        for g in range(6):
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i += 1
            text += "]"

        j -= 7
        text += "\n["
        if len(self.fields[j].pawns) > 0:
            for pawn in self.fields[j].pawns:
                text += str(pawn.belongsTo.id)
        else:
                text += " "
        text += "]                                       ["
        if len(self.fields[i].pawns) > 0:
            for pawn in self.fields[i].pawns:
                text += str(pawn.belongsTo.id)
        else:
                text += " "
        text += "]\n"

        j -= 1
        i += 1

        for g in range(6):
            text += "["
            if len(self.fields[j].pawns) > 0:
                    for pawn in self.fields[j].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            j -= 1
            text += "]"

        text += "         "
        i += 5
        for g in range(6):
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i -= 1
            text += "]"

        i += 7

        text += "\n"
        for g in range(5):
            text += "                  ["
            if len(self.fields[j].pawns) > 0:
                    for pawn in self.fields[j].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            j -= 1
            text += "]   " 
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i += 1
            text += "]\n" 

        i = j
        text += "                  "
        for g in range(3):
            text += "["
            if len(self.fields[i].pawns) > 0:
                    for pawn in self.fields[i].pawns:
                        text += str(pawn.belongsTo.id)
            else:
                text += " "
            i -= 1
            text += "]" 

        print(text)

if __name__ == "__main__":
    b = Board()

    for i in range(10):
        b.play()
