import matplotlib as plt
import math
import numpy as np




class Piece:
    def __init__(self,name,ident,char,quant,pos):
        self.name=name
        self.ident=ident
        self.char=char
        self.quant=quant
        self.pos=pos

    def __str__(self):
        return f'\n{self.name}: {self.char}\n{self.quant} pieces\npos: {self.pos}\n'
    
    def piecetoboard(self):
        put piece on board


class Board:
    def __init__(self,name,grid,gridchars):
        self.name=name
        self.grid=grid
        self.gridchars=gridchars
    
w_pawn=[]
w_knig=[]
w_rook=[]
w_bish=[]
w_king=[]
w_quen=[]

b_pawn=[]
b_knig=[]
b_rook=[]
b_bish=[]
b_king=[]
b_quen=[]

for i in range(0,8):
    w_pawn.append(Piece('Pawn',1,'♟︎',8,[i,1]))

for i in range(0,8):
    if i==(1 or 6):
        w_knig.append(Piece('Knight',2,'♞',2,[i,0]))

for i in range(0,8):
    if i==(0 or 7):
        w_rook.append(Piece('Rook',3,'♜',2,[i,0]))

for i in range(0,8):
    if i==(2 or 5):    
        w_bish.append(Piece('Bishop',4,'♝',2,[i,0]))

for i in range(0,8):
    if i==(4):
        w_king.append(Piece('King',6,'♚',1,[i,0]))

for i in range(0,8):
    if i==(3):
        w_quen.append(Piece('Queen',5,'♛',1,[i,0]))




for i in range(0,8):
    b_pawn.append(Piece('Pawn',1,'♙',8,[i,6]))

for i in range(0,8):
    if i==(1 or 6):
        b_knig.append(Piece('Knight',2,'♘',2,[i,7]))

for i in range(0,8):
    if i==(0 or 7):
        b_rook.append(Piece('Rook',3,'♖',2,[i,7]))

for i in range(0,8):
    if i==(2 or 5):  
        b_bish.append(Piece('Bishop',4,'♗',2,[i,7]))

for i in range(0,8):
    if i==(4):       
        b_king.append(Piece('King',6,'♕',1,[i,7]))

for i in range(0,8):
    if i==(3):  
        b_quen.append(Piece('Queen',5,'♔',1,[i,7]))

print(w_pawn[3])


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







