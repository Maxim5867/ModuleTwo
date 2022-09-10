import random
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
       
        