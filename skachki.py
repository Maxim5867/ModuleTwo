import random,os
#функция заставки
def zastavka():
    print()
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print()
#Настройки с выбором суммы игрока и минимальной ставки
def nastroyki():
    while True: 
        money = input('Введите сколько денег будет у игрока:')
        if not money.isdigit():
            print('Вы должны вводить только цифры.')
        else:
            money = int(money)
            break
    while True:
        minStavka = input('Введите минимальную ставку на скачках:')
        if not minStavka.isdigit():
            print('Вы должны вводить только цифры.')
        elif int(minStavka)>money:
            print('Ставка не может быть больше вашей суммы денег.')
        else:
            minStavka = int(minStavka)
            break
    return [money,minStavka]
#Предистории
def PredIst1():
    print('''Вы проснулись рано утром, готовлясь идти на ипподром.
    Когда вы пришли на скачки, познакомились с рядом стоящими людьми
    и поспорили, какя лошадь выиграет''')
def PredIst2():
    print('''Пришло время ставить на лошадей,
     вы по чуть-чуть подходите к кассе...''')
#Функции с выбором ставки и лошади
def ViborHorse():
    while True:
        vibor = input('Введите какую лошадь хотиет выбрать: 1,2,3 или 4')
        if not vibor.isdigit():
            print('Вы должны вводить только цифры')
        




























