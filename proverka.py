import random,os
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