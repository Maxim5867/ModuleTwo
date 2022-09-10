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
