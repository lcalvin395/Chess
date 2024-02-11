import matplotlib as plt
import math
import numpy as np




class Piece:
    def __init__(self,name,ident,char,quant,):
        self.name=name
        self.ident=ident
        self.char=char
        self.quant=quant

    def __str__(self):
        return f'\n{self.name}: {self.char}\n{self.quant} pieces\n'


class Board:
    def __init__(self,name,grid):
        self.name=name
        self.grid=grid
    

pawn1=Piece('Pawn',1,'♟︎',10)
knig1=Piece('Knight',2,'♞',2)
rook1=Piece('Rook',3,'♜',2)
bish1=Piece('Bishop',4,'♝',2)
king1=Piece('King',6,'♚',1)
quen1=Piece('Queen',5,'♛',1)

pawn2=Piece('Pawn',1,'♙',10)
knig2=Piece('Knight',2,'♘',2)
rook2=Piece('Rook',3,'♖',2)
bish2=Piece('Bishop',4,'♗',2)
king2=Piece('King',6,'♕',1)
quen2=Piece('Queen',5,'♔',1)

print(pawn1)



board=Board('Board',np.zeros((10,10)))

print(board.grid)






