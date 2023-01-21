import random
def StartWindow(windows):
    windows = ['''
    **********-----**********
    *  Игра: 'Виселица'     *
    *  Автор: Абдин Максим  *
    *  Версия: 2.3.0        *
    *                       *
    **********-----**********
    ''']
StartWindow =(''' 
**********-----**********
*  Игра: 'Виселица'     *
*  Автор: Абдин Максим  *                
*  Версия: 2.3.0        *                     
*        ┃┃┃┃┃┃┃┃       *
*       ╭┻┻┻┻┻┻┻╋       *
*      ╭┛╰━╯┻┻┻┻╋       *
*      ╰━┳┳━━━┳┳┛       *                                                    
**********-----**********
''')
print(StartWindow)
def sozdanieVis():
    HANGMANPICS = ['''
 +---+
     |
     |
     |
    ---''','''
 +---+
 0   |
     |
     |
    ---''','''
 +---+
 0   |
 |   |
     |
    ---''','''
 +---+
 0   |
/|   |
     |
    ---''','''
 +---+
 0   |
/|\  |
     |
    ---''','''
 +---+
 0   |
/|\  |
/    |
    ---''','''
 +---+
 0   |
/|\  |
/ \  |
    ---''','''
 +---+
[0   |
/|\  |
/ \  |
    ---''','''
+---+
[0] |
/|\ |
/ \ |
   ---''','''
+---+
[0]- |
/|\  |
/ \  |
    ---''','''
+---+
[0]- |
/|\- |
/ \  |
    ---''']    
    return HANGMANPICS

words = {'животные':'скунс баран папуас опосум бык корова козел кошка собака волк воробей гусь голубь' .split(),
'цвета':'оранжевый голубой синий бирюзовый фиолетовый черный белый коричневый зеленый красный желтый' .split(),
'овощи':'помидор огурец картофель кабачок капуста перец чеснок лук морковь' .split(),
'фигуры':'параллелограмм квадрат прямоугольник треугольник трапеция овал ромб четырехугольник' .split()}
#1 функция
def RandomWord(wordSpisok,levS):
    if levS == 'L':
        for i in range(len(list(wordSpisok.keys()))):        #range(len(list(wordSpisok.keys()))):
            print('Введите '+str(i)+' для '+list(wordSpisok.keys())[i])
        vybK = input()
        vybK = int(vybK)
        wordKey = list(wordSpisok.keys())[vybK]
    else:    
        wordKey = random.choice(list(wordSpisok.keys())) 
    wIndex = random.randint(0, len(wordSpisok[wordKey])-1)
    return [wordSpisok[wordKey][wIndex],wordKey]

def LevelVibor():
    print('Выберите уровень сложности')
    print('Введите "L" для легкого')
    print('Введите "S" для среднего')
    print('Введите "T" для тяжелого')
    while True:
        otv = input().upper()
        if len(otv) !=1:
            print('Введите только одну букву')
        elif otv not in 'LST':
            print('Введите "L", "S" или "T"')
        else:
            return otv

def deletVis(urS,hangP):
    if urS == 'S':
        del hangP[10]
        del hangP[9]
    elif urS == 'T':
        del hangP[10]
        del hangP[9]
        del hangP[8]
        del hangP[7]
#2 функция
def displayBoard(errorB,yesB,sicretS,hangP):
    print(hangP[len(errorB)])
    print()
    print('Ошибочные буквы:',end=' ')
    for letter in errorB:
        print(letter,end=' ')
    print()
    slovo = '_'*len(sicretS)
    for sl in range(len(sicretS)):
        if sicretS[sl] in yesB:
            slovo = slovo[:sl]+sicretS[sl]+slovo[sl+1:]

    for ls in slovo:
        print(ls, end=' ')
    print() 

#проверка 2 функции(3 функция)
def ProverkaVvod(Vvod):
    while True:
        Vvo = input('Введите букву')
        Vvo = Vvo.lower()
        if len(Vvo)!=1:
            print('Введите только одну букву')
        elif Vvo in Vvod:
            print('Введите букву, а не другой символ')
        elif Vvo not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Введите только букву, а не другой символ')
        else:
            return Vvo
#4 функция
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



delV = True
errorB = ''
yesB = ''
gameOver = False
while True:
    if delV:
        hm = sozdanieVis()     
        bS = LevelVibor()
        deletVis(bS,hm)
        sicretS,keyWords = RandomWord(words,bS)
        delV = False
    if bS == 'L':
        print('Категория слова: '+keyWords)
    displayBoard(errorB,yesB,sicretS,hm)
    bukva = ProverkaVvod(errorB+yesB)
    if bukva in sicretS:
        yesB = yesB + bukva
        ssYes = True
        for i in range(len(sicretS)):
            if sicretS[i] not in yesB:
                ssYes = False
                break
        if ssYes:
            displayBoard(errorB,yesB,sicretS,hm)
            print('Вы выиграли. Вы отгадали слово за '+str(len(yesB+errorB))+' количество ходов')
            gameOver = True
    else:
        errorB = errorB + bukva
        if len(errorB) == len(hm) -1:
            displayBoard(errorB,yesB,sicretS,hm)
            print('Вы проиграли. Секретное слово: '+sicretS)
            gameOver = True
            
    if gameOver:
        if playAgain():
            errorB = ''
            yesB = ''
            gameOver = False
            delV = True
        else:
            break
def StartWindow(windows):
    windows = ['''
    **********-----**********
    *  Игра: 'Виселица'     *
    *  Автор: Абдин Максим  *
    *  Версия: 2.3.0        *
    *                       *
    **********-----**********
    ''']
StartWindow =(''' 
**********-----**********
*  Игра: 'Виселица'     *
*  Автор: Абдин Максим  *                
*  Версия: 2.3.0        *                     
*        ┃┃┃┃┃┃┃┃       *
*       ╭┻┻┻┻┻┻┻╋       *
*      ╭┛╰━╯┻┻┻┻╋       * 
*      ╰━┳┳━━━┳┳┛       *                                                    
**********-----**********
''')
print(StartWindow)
