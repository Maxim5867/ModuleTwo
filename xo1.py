import random
from shutil import move
def displayBoard(pole):
    print(pole[7]+'|'+pole[8]+'|'+pole[9])
    print('-+-+-')
    print(pole[4]+'|'+pole[5]+'|'+pole[6])
    print('-+-+-')
    print(pole[1]+'|'+pole[2]+'|'+pole[3])
displayBoard(['I','O',' ','X','X','O',' ',' ','X','O'])

def viborStoroni():
    while True:
        print('Выберите за какую сторону вы хотите играть')
        print('Введите "X" или "O" на английской раскладке')
        otvet = input().upper()
        if otvet == 'X' or  otvet == 'O':
            break

    if otvet == 'X':
        return ['X','O']
    else:
        return ['O','X']
print (viborStoroni())

def WhoFirst():
    if random.randint(0,1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'
print (WhoFirst())


def makeMove(board,letter,move):
    board[move] = letter

def ProverkaWin(board,bo,le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or
    (bo[4]==le and bo[5]==le and bo[6]==le) or 
    (bo[1]==le and bo[2]==le and bo[3]==le) or 
    (bo[7]==le and bo[4]==le and bo[1]==le) or
    (bo[8]==le and bo[5]==le and bo[2]==le) or
    (bo[9]==le and bo[6]==le and bo[3]==le) or
    (bo[7]==le and bo[5]==le and bo[3]==le) or
    (bo[9]==le and bo[5]==le and bo[1]==le))
    
def CopyBoard(board):
    copyboard = [] 
    for i in board:
        copyboard.append(1)
    return copyboard

def ProvCP(board,move):
    return board[move] == ''

def MovePlayer(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not ProvCP(board,int(move)):
        print('Выберите номер ячейки(1-9)')
        move = input()
        return int(move)
def RandomList(board,movList):
    randommove = []
    for i in movList:
        if ProvCP(board,i):
            randommove.append(1)
    if len(randommove) != 0:
        return random.choice(randommove)
    else:
        return None

########################
#ОСНОВНОЕ ТЕЛО ПРОГРАММЫ 
########################


board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  
mL = [1,3,7,9]

hod = RandomList(board,mL)
makeMove(board,'O',hod)
displayBoard(board)

board[1] = 'X'
board[7] = 'X'
board[9] = 'X'
 
hod = RandomList(board,mL)
makeMove(board,'O',hod)
displayBoard(board)






    
 








