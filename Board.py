from die import Die
from pawn import Pawn
from field import Field
from player import Player

class Board:
    die = Die()
    pawns = [16]
    players = [4]
    fields = [56]

    def __init__(self):
        #Put the fields on the board
        field = Field()
        self.fields[0] = field
        for i in range(len(self.fields)-1):
            field = Field()
            self.fields[i+1] = field
            self.fields[i].next = field

        self.fields[len(self.fields)-1].next = self.fields[0]

        #Initialize the players
        for i in range(len(self.players)):
            player = Player(None, None) #Add goal and entry
            self.players[i] = player

        #Iniitalize the pawns
        gibb = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
        for i in range(len(self.pawns)):
            pawn = Pawn(self.players[gibb[i]])
            self.pawns[i] = pawn

if __name__ == "__main__":
    b = Board()