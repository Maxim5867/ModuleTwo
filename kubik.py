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
def KubikiPlay():
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
    sz = []
    k1 = random.randint(1,6)
    k2 = random.randint(1,6)
    sz.append(k1)
    sz.append(k2)
    return sz
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
def display(gamer,kubiki,kub1,kub2,sG,sK):
    print(gamer)
    print()
    print(kubiki(kub1))
    print(kubiki(kub2))
    print()
    print('У игрока - '+str(sG)+'. У компьютера - '+str(sK)+'.')

def WhoFirst():
    if random.randint(0,1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def hodP():
    print('Бросаем (Б) или передаем ход?')
    while True:
        if input(). lower().startswith('O'):
            return True
        else:
            return False
def proverkaBals(summaK,summaG):
    if summaK > 21:
        return False
    elif summaK > summaG:
        return False
    elif summaK == summaG:
        return False
    else:
        return True    



#***********************#
#Основное тело программы#
#***********************#

if vopros('Хотите прочитать правила? (да или нет)'):
    pravilaGame()

ktoBrosaet = 'Человек'
kub = brosok()
summaK = 0
summaG = 0
game = True
gamer = True
komputer = True
pris = True


while game:
    while gamer:
        kub1,kub2 = brosok()
        summaG = summaG + kub1 + kub2
        display(kub,kub1,kub2,summaG,summaK)
        if summaG > 21:
            print('Вы проиграли')
            game = False
            gamer = False
        if game and not (input('(Б)росаем еще или передаем ход?').upper() == 'Б'):
            gamer = False

    print('Передаем ход')

    ktoBrosaet = 'Компьютер'
    while komputer:
        kub1,kub2 = brosok()
        summaK = summaK + kub1 + kub2
        display(kub,kub1,kub2,summaG,summaK)
        s = input('Для продолжения нажмите Enter')
        komputer = proverkaBals(summaG,summaK)
    
    if  summaK > 21:
        print('Поздравляю! Вы выиграли')
    elif summaK > summaG:
        print('Увы! Вы проиграли')
    elif summaK == summaG:
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