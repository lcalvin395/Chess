import matplotlib.pyplot as plt
import math
import numpy as np
import keyboard
import time




class Piece:
    def __init__(self,name,ident,char,quant,posx, posy,xymove,xybigmove):
        self.name=name
        self.ident=ident
        self.char=char
        self.quant=quant
        self.posx=posx
        self.posy=posy
        self.xymove=xymove
        self.xybigmove=xybigmove

    def __str__(self):
        return f'\n{self.name}: {self.char}\n{self.quant} pieces\nposx: {self.posx}\nposy: {self.posy}\n'
    
    def piecetoboard(self):

        board.grid[self.posy][self.posx]=self.name,self.ident,self.char,self.quant,self.posx, self.posy, self.xymove, self.xybigmove
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
                    if event.name=='e':
                        xy.append((event.name))
                        print(xy[0], end="\r", flush=True)   
                    else:
                        xy.append(int(event.name))
                        print(xy[0], end="\r", flush=True)
                if n==1:
                    if event.name=='x':
                        xy.append((event.name))
                        print(xy[0], end="", flush=True)
                        print(xy[1], end="\r", flush=True)
                
                    else:
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


xdiff=0
ydiff=0


for i in range(0,8):
    w_pawn.append(Piece('w-Pawn',1,'♟︎',8,i,1,[[0,-1],[-1,-1],[1,-1]],0))
    w_pawn[len(w_pawn)-1].piecetoboard()



for i in range(0,8):
    if i==1 or i==6:
        w_knig.append(Piece('w-Knight',2,'♞',2,i,0,[[2,-1],[-2,-1],[2,1],[-2,1],[-1,-2],[1,-2],[-1,2],[1,2]],0))
        w_knig[len(w_knig)-1].piecetoboard()

for i in range(0,8):
    if i==0 or i== 7:
        w_rook.append(Piece('w-Rook',3,'♜',2,i,0,[[1,0],[0,1]],1))
        w_rook[len(w_rook)-1].piecetoboard()

for i in range(0,8):
    if i==2 or i==5:    
        w_bish.append(Piece('w-Bishop',4,'♝',2,i,0,[[1,1]],2))
        w_bish[len(w_bish)-1].piecetoboard()

for i in range(0,8):
    if i==(4):
        w_king.append(Piece('w-King',6,'♚',1,i,0,[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]],0))
        w_king[len(w_king)-1].piecetoboard()

for i in range(0,8):
    if i==(3):
        w_quen.append(Piece('w-Queen',5,'♛',1,i,0,[[1,1],[1,0],[0,1]],1))
        w_quen[len(w_quen)-1].piecetoboard()




for i in range(0,8):
    b_pawn.append(Piece('b-Pawn',1,'♙',8,i,6,[[0,1],[1,1],[-1,1]],0))
    b_pawn[len(b_pawn)-1].piecetoboard()

for i in range(0,8):
    if i==1 or i==6:
        b_knig.append(Piece('b-Knight',2,'♘',2,i,7,[[2,-1],[-2,-1],[2,1],[-2,1],[-1,-2],[1,-2],[-1,2],[1,2]],0))
        b_knig[len(b_knig)-1].piecetoboard()

for i in range(0,8):
    if i==0 or i==7:
        b_rook.append(Piece('b-Rook',3,'♖',2,i,7,[[1,0],[0,1]],1))
        b_rook[len(b_rook)-1].piecetoboard()


for i in range(0,8):
    if i==2 or i==5:  
        b_bish.append(Piece('b-Bishop',4,'♗',2,i,7,[[1,1]],2))
        b_bish[len(b_bish)-1].piecetoboard()

for i in range(0,8):
    if i==(4):       
        b_king.append(Piece('b-King',6,'♕',1,i,7,[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]],0))
        b_king[len(b_king)-1].piecetoboard()

for i in range(0,8):
    if i==(3):  
        b_quen.append(Piece('b-Queen',5,'♔',1,i,7,[[1,1],[1,0],[0,1]],1))
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
'''00
03
for i in range(3):
    reprint('BOOTING UP CHESS.')
    time.sleep(0.2)
    reprint('BOOTING UP CHESS..')
    time.sleep(0.2)
    reprint('BOOTING UP CHESS...')
    time.sleep(0.2)
print('                            ')
print('BOOTED!\n')
for i in range(3):
    reprint('CONSTRUCTING BOARD.')
    time.sleep(0.2)
    reprint('CONSTRUCTING BOARD..')
    time.sleep(0.2)
    reprint('CONSTRUCTING BOARD...')
    time.sleep(0.2)
print('                          ')
print('CONSTRUCTED!\n')
for i in range(3):
    reprint('RECRUITING PIECES.')
    time.sleep(0.2)
    reprint('RECRUITING PIECES..')
    time.sleep(0.2)
    reprint('RECRUITING PIECES...')
    time.sleep(0.2)
print('                        ')
print('RECRUITED!\n')'''




whoseturn=0    #    0 is white   ::::    1 is black

o=0
while o==0:
        
    print('\n',board.disp,'\n')

    if whoseturn==0:
        print('WHITE\'S TURN')
    if whoseturn==1:
        print('BLACK\'S TURN')

    print('Move which piece?')

    xy=inputxy()
    if xy==['e','x']:
        break
    if whoseturn==0 and board.grid[xy[1],xy[0]][0][0]!='w':
        print('\nWRONG COLOUR\n')
        continue
    
    if whoseturn==1 and board.grid[xy[1],xy[0]][0][0]!='b':
        print('\nWRONG COLOUR\n')
        continue


    print('xy: ',xy)
    print(board.disp,'\n')
    print('Move',(board.grid[xy[1],xy[0]][0]),'where?')
    print(board.grid[xy[1],xy[0]])

    newxy=inputxy()

    if board.grid[newxy[1],newxy[0]]!=0:
        if board.grid[xy[1],xy[0]][0][0]==board.grid[newxy[1],newxy[0]][0][0]:
            print('THIS IS A FRIENDLY PIECE!')

    xydir=[0,0]



    xydiff=[int(newxy[0]-xy[0]),int(newxy[1]-xy[1])]

    if xydiff[0]==0:
        xydir[0]=0
    else:
        xydir[0]=int(xydiff[0]/abs(xydiff[0]))

    if xydiff[1]==0:
        xydir[1]=0
    else:
        xydir[1]=int(xydiff[1]/abs(xydiff[1]))

    #xydir=[xydiff[0]/abs(xydiff[0]),xydiff[1]/abs(xydiff[1])]



    bigmove=board.grid[xy[1],xy[0]][7]

    print((xy))
    print((xy))
    #if nothing between where piece is and where it wants to go (and its not knight):#
    if (board.grid[xy[1],xy[0]][0] == 'w-Knight') or (board.grid[xy[1],xy[0]][0] == 'b-Knight'):
        for i in range(0,len(board.grid[xy[1],xy[0]][6])):
            if bigmove==0:
                if (xydiff == board.grid[xy[1],xy[0]][6][i]) or (abs(xydiff[0])/abs(xydiff[1])==board.grid[xy[1],xy[0]][6][i][0]/board.grid[xy[1],xy[0]][6][i][1]) :
                    board.disp[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]][2]
                    board.disp[xy[1],xy[0]]='☐'
                    board.grid[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]]
                    board.grid[xy[1],xy[0]]=0
                    break
            if bigmove==1:
                if ((xydiff[0]==0) or (xydiff[1]==0)) and  ((board.grid[xy[1],xy[0]][6][i][0]==0) or (board.grid[xy[1],xy[0]][6][i][1]==0)):
                    board.disp[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]][2]
                    board.disp[xy[1],xy[0]]='☐'
                    board.grid[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]]
                    board.grid[xy[1],xy[0]]=0
                    break
    else:
        breakout=1
        xycheck=xy[:]
        while ((xycheck[1]!=newxy[1]-xydir[1]) or (xycheck[0]!=newxy[0]-xydir[0])):           #Checking if move is being blocked by another piece
            print('xycheck:',xycheck)
            xycheck[1]=xycheck[1]+xydir[1]
            xycheck[0]=xycheck[0]+xydir[0]
            print('xycheck:',xycheck)
            if board.grid[xycheck[1],xycheck[0]]!=0:
                breakout=0     
                print('move blocked')  
                                                          
        if breakout==1:
            print((xy))
            for i in range(0,len(board.grid[xy[1],xy[0]][6])):
                if bigmove==0:
                    if (xydiff == board.grid[xy[1],xy[0]][6][i]) or (abs(xydiff[0])/abs(xydiff[1])==board.grid[xy[1],xy[0]][6][i][0]/board.grid[xy[1],xy[0]][6][i][1]) :
                        board.disp[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]][2]
                        board.disp[xy[1],xy[0]]='☐'
                        board.grid[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]]
                        board.grid[xy[1],xy[0]]=0
                        break
                if bigmove==1:
                    if ((xydiff[0]==0) or (xydiff[1]==0)) and  ((board.grid[xy[1],xy[0]][6][i][0]==0) or (board.grid[xy[1],xy[0]][6][i][1]==0)):
                        board.disp[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]][2]
                        board.disp[xy[1],xy[0]]='☐'
                        board.grid[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]]
                        board.grid[xy[1],xy[0]]=0
                        break
                if bigmove==2:
                    if (abs(xydiff[0])==abs(xydiff[1])):
                        board.disp[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]][2]
                        board.disp[xy[1],xy[0]]='☐'
                        board.grid[newxy[1],newxy[0]]=board.grid[xy[1],xy[0]]
                        board.grid[xy[1],xy[0]]=0
                        break
    whoseturn=1-whoseturn

'''if event.name == 'n':
        print(event.name)
        break'''