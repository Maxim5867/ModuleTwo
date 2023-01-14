import random
def displayBoard(pole):
    print(pole[7]+'|'+pole[8]+'|'+pole[9])
    print('-+-+-')
    print(pole[4]+'|'+pole[5]+'|'+pole[6])
    print('-+-+-')
    print(pole[1]+'|'+pole[2]+'|'+pole[3])

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

def WhoFirst():
    if random.randint(0,1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def makeMove(board,letter,move):
    board[move] = letter

def ProverkaWin(bo,le):
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
        copyboard.append(i)
    return copyboard

def ProvCP(board,move):
    return board[move] == ' '

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
            randommove.append(i)

    if len(randommove) != 0:
        return random.choice(randommove)
    else:
        return None

########################
#ОСНОВНОЕ ТЕЛО ПРОГРАММЫ 
########################


def ComputerMove(board,computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    
    for i in range(1,10):
        copyboard = CopyBoard(board)
        if ProvCP(board,i):
            makeMove(copyboard,computerLetter,i)
            if ProverkaWin(copyboard,computerLetter):
                return i
    
    for i in range(1,10):
        copyboard = CopyBoard(board)
        if ProvCP(board,i):
            makeMove(copyboard,playerLetter,i)
            if ProverkaWin(copyboard,playerLetter):
                return i
    
    move = RandomList(board,[1,3,7,9])
    if move != None:
        return move
    
    if ProvCP(board,5):
        return 5
    
    return RandomList(board,[2,4,6,8])
def isBoardFull(board):
    for i in range(1,10):
        if ProvCP(board,i):
            return False
    return True
    
########################
#ОСНОВНОЕ ТЕЛО ПРОГРАММЫ 
########################

print('Игра Крестики-Нолики')

while True:
    TheBoard = [' ']*10
    playerLetter, computerLetter = viborStoroni()

    turn = WhoFirst()
    print(''+turn+'ходи первым')

    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            displayBoard(TheBoard)
            move = MovePlayer(TheBoard)
            makeMove(TheBoard,playerLetter,move)

            if ProverkaWin(TheBoard,playerLetter):
                displayBoard(TheBoard)
                print('Поздравляю!Ты выиграл')
                gameIsPlaying = False
            else:
                if isBoardFull(TheBoard):
                    displayBoard(TheBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Компьютер'
        else:
            move  = ComputerMove(TheBoard,computerLetter)
            makeMove(TheBoard,computerLetter,move)

            if ProverkaWin(TheBoard,computerLetter):
                displayBoard(TheBoard)
                print('ИИ был сильнее! Вы проиграли')
                gameIsPlaying = False
            else:
                if isBoardFull(TheBoard):
                    displayBoard(TheBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем еще раз?(да или нет)')
    if not input(). lower(). startswith('д'):
        break
 #la#