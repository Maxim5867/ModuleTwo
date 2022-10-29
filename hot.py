from inspect import GEN_CLOSED
import random

#*********#
#Константы#
#*********# 

KOL_CIFR = 3
KOL_POP = 10

#************#
#Функции кода#
#************#

def GenNumber():
    chislo = list(range(10))
    random.shuffle(chislo)
    secretCh = ''
    for i in range(KOL_CIFR):
        secretCh += str(chislo[i])
    return secretCh

def Podskazka(chislo_games,chislo_komp):
    if chislo_games ==chislo_komp:
        return 'Вы угадали!'
    podskazka = []
    for i in range(len(chislo_games)):
        if chislo_games[i] == chislo_komp[i]:
            podskazka.append('Горячо')
        elif chislo_games[i] in chislo_komp:
            podskazka.append('Тепло')


    if len(podskazka) == 0:
        return 'холодно'        
    
    podskazka.sort()
    return ' '.join(podskazka)

def Proverka_vvoda(num):
    if num == '':
        return False

    for i in num:
        if num not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False  

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



#***********************#
#Основное тело программы#
#***********************#

print('Я загадаю %s-x значное число, которое вы должны отгодать' % (KOL_CIFR))
print('Я дам вам несколько подсказок')
print('Если я говорю:                Это значит:')
print('   Горячо                     Отгадана цифра и ее позиция')
print('   Тепло                     Отгадана цифра, но не ее позиция')
print('   Холодно                     Не отгадана ни одна цифра')

while True:
    secretNum = GenNumber()

    print('Итак, я загадал число. У вас есть %s попыток, чтобы отгдать его.' %(KOL_POP))

    popytka = 1
    while popytka <= KOL_POP:
        chislo_games = ''
        while len(chislo_games) !=KOL_CIFR or not Proverka_vvoda(chislo_games):
            print('Попытка & %s:' %(popytka))
            chislo_games = input()
    
        print(Podskazka)

    if not playAgain():
        break                         
