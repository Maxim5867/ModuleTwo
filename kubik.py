import random
#*************************************#
#Начальное окно для пердстваления игры#
#*************************************#
def StartWindow(windows):
    windows = ['''
    **********-----**********
    *  Игра: 'Кубики'       *
    *  Автор: Абдин Максим  *
    *  Версия: 2.3.0        *
    *                       *
    **********-----**********
    ''']
StartWindow =(''' 
**********-----**********
*  Игра: 'Кубики'       *
*  Автор: Абдин Максим  *                
*  Версия: 2.3.0        *                     
*                       *                        
**********-----**********
''')
print(StartWindow)
#***************************#
#Функция изобретения кубиков#
#***************************#
def kubiki():
    kubiki = ['''
     ...
    |   |
    |   |
    |   |''','''
     ***
     ...
    |   |
    | * |
    |   |''','''
     ***
     ...
    |   |
    |* *|
    |   |''','''
     ***
     ...
    |*  |
    | * |
    |  *|''','''
     ***
     ...
    |* *|
    |   |
    |* *|''','''
     ***
     ...
    |* *|
    | * |
    |* *|''','''
     ***
     ...
    |* *|
    |* *|
    |* *|
     *** ''']
    return kubiki
#*******************#
#Функция с правилами#
#*******************#
def brosok():
    k1 = random.randint(1,6)
    k2 = random.randint(1,6)
    kub = []
    kub.append(k1)
    kub.append(k2)
    return kub

def playAgain():
    print('Хотите ли вы сыграть ещё? Да или нет')
    while True:
        otvet = input(). lower()
        if(otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            return True
        elif(otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        else:
            print('''Я вас не понял, напишите пожалуйста да или нет''')


def vopros(TextVoprosa):
    while True:
        print(TextVoprosa)
        otvet = input()
        otvet = otvet.lower()
        if (otvet == 'да' ) or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            return True
        elif (otvet == 'нет' ) or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        else:
            print('Я вас не понял! Введте ответ еще раз')

def pravilaGame():
    print('''Представляю вам правила игры кубикию. Игрок и компьтер поочередно пытаються набрать 21 очко,
             бросая два кубика.
            Человек начинаете первый, вы можете бросать кубики до тех пора не наберете 21 очко.
            Но учтите, если вы наберете больше 21 очка, сразу проиграете.
            Когда вы набрали определенное число,которым вы удовлетворены, можете передать ход компьютеру.
            Он будет кидать кубики до тех пор, пока не наберет число больше вашего.
            Если наберет больше 21, он програет, а вы выиграете.
            После вы сможете продолжить играть, если захотите''')
    print()
    s = input('Для продолжения нажмите Enter')

def display(kubiki,kub1,kub2,balG,balK,gamer):
    print(kubiki[kub1])
    print(kubiki[kub2])
    print(gamer)
    print()
    print('Количество очков')
    print('У игрока - '+str(balG)+'. У компьютера - '+str(balK)+'.')



def hodP():
    print('Бросаем (Б) или передаем ход?')
    while True:
        if input(). lower().startswith('O'):
            return True
        else:
            return False

def proverkaBals(bK,bG):
    if bK > 21:
        return False
    elif bK > bG:
        return False
    elif bK == bG:
        return False
    else:
        return True    



#***********************#
#Основное тело программы#
#***********************#

if vopros('Хотите прочитать правила? (да или нет)'):
    pravilaGame()


gamer = 'Человек'
kub = brosok()
bK = 0
bG = 0
game = True
gamer = True
komputer = True
pris = True


while game:
    while gamer:
        o1,o2 = brosok()
        bG = bG + o1 + o2
        display(kub,o1,o2,bG,bK,gamer)
        if bG > 21:
            print('Вы проиграли')
            game = False
            komputer = False
        if game and not (input('(Б)росаем еще или передаем ход?').upper() == 'Б'):
            pris = False

    print('Передаем ход')

    gamer = 'Компьютер'
    while komputer:
        o1,o2 = brosok()
        bK = bK + o1 + o2
        display(kub,o1,o2,bG,bK,gamer)
        s = input('Для продолжения нажмите Enter')
        komputer = proverkaBals(bG,bK)
    
    if  bK > 21:
        print('Поздравляю! Вы выиграли')
    elif bK > bG:
        print('Увы! Вы проиграли')
    elif bK == bG:
        print('Ничья')



    print('Хочешь сыграть еще?(да или нет)')
    otvet = input()
    if otvet == 'нет':
        break           



























    




    









































def playAgain():
    print('Хотите ли вы сыграть ещё? Да или нет')
    while True:
        otvet = input(). lower()
        if(otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            return True
        elif(otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        else:
            print('''Я вас не понял, напишите пожалуйста да или нет''')