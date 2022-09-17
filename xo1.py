import random
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

def RedaktSl(board,letter,move):
    board[move] = letter
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
displayBoard(board)   
redakt = input('Введите число от 1 до 9')
redakt = 5



def ProverkaWin(board,bo,le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or
    (bo[4]==le and bo[5]==le and bo[6]==le) or 
    (bo[1]==le and bo[2]==le and bo[3]==le) or 
    (bo[7]==le and bo[4]==le and bo[1]==le) or
    (bo[8]==le and bo[5]==le and bo[2]==le) or
    (bo[9]==le and bo[6]==le and bo[3]==le) or
    (bo[7]==le and bo[5]==le and bo[3]==le) or
    (bo[9]==le and bo[5]==le and bo[1]==le))
    print(ProverkaWin(board,'X'))
board[3] = 'X'
board[5] = 'X'
board[7] = 'X'
displayBoard(board)
print(ProverkaWin(board,'X',True))





