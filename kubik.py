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
    |   |
     ... ''','''
     ...
    |   |
    | * |
    |   |
     ... ''','''
     ...
    |   |
    |* *|
    |   |
     ... ''','''
     ...
    |*  |
    | * |
    |  *|
     ... ''','''
     ...
    |* *|
    |   |
    |* *|
     ... ''','''
     ...
    |* *|
    | * |
    |* *|
     ... ''','''
     ...
    |* *|
    |* *|
    |* *|
     ... ''']
    return kubiki

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
        otvet = input()
        otvet = otvet.lower()
        if(otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            return True
        elif(otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        else:
            print('''Я вас не понял, напишите пожалуйста да или нет''')

def vHelp():
    print('Хотите ли вы прочитать правила?')
    while True:
        otvet = input()
        otvet = otvet.lower()
        if (otvet == 'да' ) or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            return True
        elif (otvet == 'нет' ) or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            return False
        else:
            print('Я вас не понял! Введите ответ еще раз')

def pravilaGame():
    print('''Представляю вам правила игры кубики. Игрок и компьютер поочередно пытаються набрать 21 очко,
             бросая два кубика.
            Человек начинает первый, вы можете бросать кубики до тех пор, пока не наберете 21 очко.
            Но учтите, если вы наберете больше 21 очка, сразу проиграете.
            Когда вы набрали определенное число,которым вы удовлетворены, можете передать ход компьютеру.
            Он будет кидать кубики до тех пор, пока не наберет число больше вашего.
            Если наберет больше 21, он проиграет, а вы выиграете.
            После вы сможете продолжить играть, если захотите''')
    print()
    

def display(kubiki,kub1,kub2,balG,balK,gamer):
    print(gamer)
    print(kubiki[kub1])
    print(kubiki[kub2])
    print()
    print('Количество очков')
    print('Человек - '+str(balG)+'. Компьютер - '+str(balK)+'.')

def hodP():
    print('Бросаем (Б) или передаем ход?')
    while True:
        if input(). lower().startswith('б'):
            return True
        else:
            return False

def proverkaBals(bG,bK):
    if bK > 21:
        return False
    elif bK > bG:
        return False
    elif bK == bG:
        return False
    else:
        return True    


kub = kubiki()

games = True
while games:
    if vHelp():
        pravilaGame()
        s = input('Для продолжения нажмите Enter.')


    gamer ='Человек'
    bG = 0
    bK = 0
    g = True
    gK = True


    pris = True


    gamer ='Человек'
    bG = 0
    bK = 0
    g = True
    gK = True

    pris = True


    while g:
        o1,o2 = brosok()
        bG = bG + o1 + o2
        display(kub,o1,o2,bG,bK,gamer)

        if bG > 21:
            print('Увы! Вы проиграли!')
            g = False
            gK = False
            pris = False
        else:
            g = hodP()
    
    gamer = 'Компьютер'

    while gK:

        o1,o2 = brosok()
        bK = bK + o1 + o2
        display(kub,o1,o2,bG,bK,gamer)

        s = input('Для продолжения нажмите Enter.')

        gK = proverkaBals(bG,bK)

    
    if bK > 21:
        print('Поздравляю! Вы выиграли!')
    elif bK > bG:
        print('Увы! Вы проиграли!')
    elif bK == bG:
        print('Ничья')
    
    games = playAgain()



























    




    










































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

            print('''Я вас не понял, напишите пожалуйста да или нет''')