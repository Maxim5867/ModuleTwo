import random

ocenka = 0
uroven = 1
otvet = 0

for i in range(1,4):
    if uroven == 1:
        a = random.randint(1,9)
        b = random.randint(1,9)
    elif uroven == 2:
        a = random.randint(10,99)
        b = random.randint(10,99)
    elif uroven == 3:
        a = random.randint(100,999)
        b = random.randint(100,999)

    print('Сложите в уме числа %s и %s и напишите ответ' % (str(a),str(b)))
    sum = input()
    
    if str(a+b) == sum:
        print('Молодец! Ответ верный')
        uroven += 1
        otvet += 1
        ocenka += 5
    else:
        print('Ответ не верный, попробуй еще')
        ocenka += 2

ocenka /= 3

if otvet == 1:
    vopros = 'вопрос'
else:
    vopros = 'вопроса'


print('Ты правильно ответил на %s %s из 3. Оценка - "%s"' % (str(otvet),vopros,ocenka))
        

