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
    def __init__(self,name,grid,gridchars):
        self.name=name
        self.grid=grid
        self.gridchars=gridchars
    

pawn1=Piece('Pawn',1,'♟︎',8)
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



board=Board('Board',np.zeros((8,8)),np.zeros((8,8)))

print(board.grid,'\n\n\n')

'''board.grid=[[3, 2, 4, 5, 6, 4, 2, 3][1, 1, 1, 1, 1, 1, 1, 1] [0, 0, 0, 0, 0, 0, 0, 0,]
 [0, 0, 0, 0, 0, 0, 0, 0,]
 [0, 0, 0, 0, 0, 0, 0, 0,]
 [0, 0, 0, 0, 0, 0, 0, 0,][1, 1, 1, 1, 1, 1, 1, 1][3, 2, 4, 5, 6, 4, 2, 3]]'''

board.grid[0]=[3, 2, 4, 5, 6, 4, 2, 3]
board.grid[1]=np.ones(8)
board.grid[6]=np.ones(8)
board.grid[7]=[3, 2, 4, 5, 6, 4, 2, 3]

print(board.grid)

for i in range(0,len(board.grid[0])):
    for j in range(0,len(board.grid[0])):
        if i< 2:
            if pawn1.ident==board.grid[i,j]:
                board.gridchars[i,j]= pawn1.char







