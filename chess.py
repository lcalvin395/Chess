import matplotlib.pyplot as plt
import math
import numpy as np
import keyboard
import time




class Piece:
    def __init__(self,name,ident,char,quant,posx, posy):
        self.name=name
        self.ident=ident
        self.char=char
        self.quant=quant
        self.posx=posx
        self.posy=posy

    def __str__(self):
        return f'\n{self.name}: {self.char}\n{self.quant} pieces\nposx: {self.posx}\nposy: {self.posy}\n'
    
    def piecetoboard(self):

        board.grid[self.posy][self.posx]=self.name,self.ident,self.char,self.quant,self.posx, self.posy
        board.disp[self.posy][self.posx]=self.char

class Board:
    def __init__(self,name,grid,disp):
        self.name=name
        self.grid=grid
        self.disp=disp




def reprint(msg, finish=False): 
    global _last_print_len 
     
    print(' '*_last_print_len, end='\r') 
     
    if finish: 
        end = '\n' 
        _last_print_len = 0 
    else: 
        end = '\r' 
        _last_print_len = len(msg) 
     
    print(msg, end=end)

def inputxy():
    print('Enter X and Y value followed by enter: \n')
    xy=[]
    n=0
    print('__', end="\r", flush=True)
    while True:
        if n<0:
            n=0
        if n>2:
            n=2
        try:
            event = keyboard.read_event()
            if event.event_type == 'down':
                if event.name=='backspace':
                    n=n-1
                    xy.pop(n)
                    print('__', end="\r", flush=True)
                    try:

                        print(xy[0], end="\r", flush=True)
                    except:
                        continue
                    try:
                        print(xy[1], end="\r", flush=True)
                    except:
                        continue
                    continue
                if n==0:
                    xy.append(int(event.name))
                    print(xy[0], end="\r", flush=True)
                if n==1:
                    xy.append(int(event.name))
                    #print(event.name, end="", flush=True)
                    print(xy[0], end="", flush=True)
                    print(xy[1], end="\r", flush=True)
                if n==2 and event.name=='enter':
                    print('\n')
                    break
                #print(xy, end="\r", flush=True)
                n+=1
        except:
            print('Correct input is 2 numbers followed by enter......\nTry again.')
            print('Enter X and Y value of piece you want to move followed by enter: \n')
            print('__',end="\r", flush=True)
            continue
    #print(xy[:], end="", flush=True)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    return(xy)




_last_print_len=0
board=Board('Board',np.zeros((8,8),dtype=dict),np.zeros((8,8),dtype=dict))

#print(board.grid,'\n\n\n')

'''board.grid=[[3, 2, 4, 5, 6, 4, 2, 3][1, 1, 1, 1, 1, 1, 1, 1] [0, 0, 0, 0, 0, 0, 0, 0,]
 [0, 0, 0, 0, 0, 0, 0, 0,]
 [0, 0, 0, 0, 0, 0, 0, 0,]
 [0, 0, 0, 0, 0, 0, 0, 0,][1, 1, 1, 1, 1, 1, 1, 1][3, 2, 4, 5, 6, 4, 2, 3]]'''

'''board.grid[0]=[3, 2, 4, 5, 6, 4, 2, 3]
board.grid[1]=np.ones(8)
board.grid[6]=np.ones(8)
board.grid[7]=[3, 2, 4, 5, 6, 4, 2, 3]'''


    
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
    w_pawn.append(Piece('Pawn',1,'♟︎',8,i,1))
    w_pawn[len(w_pawn)-1].piecetoboard()



for i in range(0,8):
    if i==1 or i==6:
        w_knig.append(Piece('Knight',2,'♞',2,i,0))
        w_knig[len(w_knig)-1].piecetoboard()

for i in range(0,8):
    if i==0 or i== 7:
        w_rook.append(Piece('Rook',3,'♜',2,i,0))
        w_rook[len(w_rook)-1].piecetoboard()

for i in range(0,8):
    if i==2 or i==5:    
        w_bish.append(Piece('Bishop',4,'♝',2,i,0))
        w_bish[len(w_bish)-1].piecetoboard()

for i in range(0,8):
    if i==(4):
        w_king.append(Piece('King',6,'♚',1,i,0))
        w_king[len(w_king)-1].piecetoboard()

for i in range(0,8):
    if i==(3):
        w_quen.append(Piece('Queen',5,'♛',1,i,0))
        w_quen[len(w_quen)-1].piecetoboard()




for i in range(0,8):
    b_pawn.append(Piece('Pawn',1,'♙',8,i,6))
    b_pawn[len(b_pawn)-1].piecetoboard()

for i in range(0,8):
    if i==1 or i==6:
        b_knig.append(Piece('Knight',2,'♘',2,i,7))
        b_knig[len(b_knig)-1].piecetoboard()

for i in range(0,8):
    if i==0 or i==7:
        b_rook.append(Piece('Rook',3,'♖',2,i,7))
        b_rook[len(b_rook)-1].piecetoboard()


for i in range(0,8):
    if i==2 or i==5:  
        b_bish.append(Piece('Bishop',4,'♗',2,i,7))
        b_bish[len(b_bish)-1].piecetoboard()

for i in range(0,8):
    if i==(4):       
        b_king.append(Piece('King',6,'♕',1,i,7))
        b_king[len(b_king)-1].piecetoboard()

for i in range(0,8):
    if i==(3):  
        b_quen.append(Piece('Queen',5,'♔',1,i,7))
        b_quen[len(b_quen)-1].piecetoboard()



for i in range(0,8):
    for j in range(0,8):
        if board.disp[i][j]==0:
            board.disp[i][j]='☐'





#w_pawn[1].piecetoboard()
#print(board.grid[0][1])
#print(board.disp)


'''w_pawn.piecetoboard()
w_knig.piecetoboard()
w_rook.piecetoboard()
w_bish.piecetoboard()
w_king.piecetoboard()
w_quen.piecetoboard()

b_pawn.piecetoboard()
b_knig.piecetoboard()
b_rook.piecetoboard()
b_bish.piecetoboard()
b_king.piecetoboard()d
b_quen.piecetoboard()'''








'''for i in range(0,len(board.grid[0])):
    for j in range(0,len(board.grid[0])):
        if i< 2:
            if pawn1.ident==board.grid[i,j]:
                board.gridchars[i,j]= pawn1.char'''
########################################################
################ Start of Main Script ##################
#########################################################
for i in range(5):
    reprint('BOOTING UP CHESS.')
    time.sleep(0.2)
    reprint('BOOTING UP CHESS..')
    time.sleep(0.2)
    reprint('BOOTING UP CHESS...')
    time.sleep(0.2)
print('                            ')
print('BOOTED!\n')
for i in range(5):
    reprint('CONSTRUCTING BOARD.')
    time.sleep(0.2)
    reprint('CONSTRUCTING BOARD..')
    time.sleep(0.2)
    reprint('CONSTRUCTING BOARD...')
    time.sleep(0.2)
print('                          ')
print('CONSTRUCTED!\n')
for i in range(5):
    reprint('RECRUITING PIECES.')
    time.sleep(0.2)
    reprint('RECRUITING PIECES..')
    time.sleep(0.2)
    reprint('RECRUITING PIECES...')
    time.sleep(0.2)
print('                        ')
print('RECRUITED!\n')
print(board.disp,'\n')

print('Move which piece?')
xy=inputxy()
print('xy: ',xy)
print(board.grid[xy[1],xy[0]])

'''if event.name == 'n':
        print(event.name)
        break'''