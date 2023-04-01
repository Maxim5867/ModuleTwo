import random,math,sys
#*****************#
#ФУНКЦИИ ПРОГРАММЫ#
#*****************#
def getPlayPole():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0,1)==0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def displayBoard(board):
    str0ne = '   '
    for i in range(1,6):
        str0ne += ' '*9 +str(i)
    
    print(str0ne)
    print('   '+('0123456789'*6))
    print()
    
    for stroka in range(15):
        if stroka<10:
            strPol = ' '
        else:
            strPol = ''

        strBoard = ''
        for stolbec in range(60):
            strBoard += board[stolbec][stroka]
        
        print('%s%s %s %s' % (strPol,stroka, strBoard,stroka))

    print()
    print('   '+('0123456789'*6))
    print(str0ne)


def getRandomChests(kolChests):
    chasts = []
    while len(chasts)<=kolChests:
        newChasts = [random.randint(0,59),random.randint(0,14)]
        if newChasts not in chasts:
            chasts.append(newChasts)
    return chasts

def vopros(textVoprosa):
    print(textVoprosa)
    while True:
        otvet = input()
        otvet = otvet.lower()
        if (otvet == 'да' ) or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            return True
        elif (otvet == 'нет' ) or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        else:
            print('Я вас не понял! Введите ответ еще раз')

def isOnBoard(x,y):
    return x>=0 and x<=59 and y>=0 and y<=14

def makeMove(board,chests,x,y):
    minDistance = 100
    for cx,cy in chests:
        distanciya = math.sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y))
        if distanciya < minDistance:
            minDistance = distanciya
    minDistance = round(minDistance)

    if minDistance == 0:
        chests.remove([x,y])
        return 'Вы нашли сундук с сокровищами на затонувшем корабле.'
    else:
        if minDistance < 10:
            board[x][y] = str(minDistance)
            return 'Сундук с сокровищами обнаружен на расстоянии %s единиц от гидролокатора.' % (minDistance)
        else:
            board[x][y] = 'X'
            return 'Гидролокатор ничего не обнаружил. Все сундуки с сокровищаи вне пределов досягаемости'  

def enterPlayerMove(predHoda):
    print('''Где следует опустить гидролокатор?
    (координаты: 0-59 0-14)
    (или наберите "Выход" для прекращения игры).''')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Спасибо за игру')
            sys.exit()

        move =  move.split()

        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]),int(move[1])):
            if [int(move[0]),int(move[1])] in predHoda:
                print('Вы уже опускали сюда гидролокатор')
            else:
                return [int(move[0]),int(move[1])]
        else:
            print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14.')

#***********************#
#ОСНОВНОЕ ТЕЛО ПРОГРАММЫ#
#***********************#




while True:
    kolGidro = 20
    theBoard = getPlayPole()
    sunduki = getRandomChests(3)
    displayBoard(theBoard)
    print()
    hodyGamer = []

    while kolGidro > 0:
        if len(sunduki)==1:
            okon = ''
        else:
            okon = 'a'
        print('Осталось %s неиспользованных гидролокаторов. Необходимо найти еще %s сундук%s.' % (kolGidro,len(sunduki),okon))
        x,y = enterPlayerMove(hodyGamer)
        hodyGamer.append([x,y])


        if makeMove(theBoard,sunduki,x,y):
            for x,y in hodyGamer:
                makeMove(theBoard,sunduki,x,y)
        displayBoard(theBoard)
        if len(sunduki) == 0:
            print('Вы нашли все сундуки с сокровищами. Поздравляю!')
            break

        kolGidro -= 1

    if kolGidro == 0:
        print('''    Все гидролокаторы опущены на дно
        Разворачиваем корабль и отправляемся домой.
        Игра окончена!''')
        print()
        print('       Вы не нашли сундуки в следующих местах')
        for x,y in sunduki:
            print(' %s, %s' % (x,y))

    if not vopros('Хотите ли вы сыграть еще раз?'):

        sys.exit()    

        sys.exit()   
