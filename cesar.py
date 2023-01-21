
SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@"#№#$;%^:&?*()-_=+\/|\/,.><''`~][}{'
MAX_SIZE_KEY = len(SYMBOLS)

def getMode():
    print('Вы хотите зашифровать, расшифровать или взломать текст?')
    while True:
        mode = input().lower()    
        if mode in ['зашифровать','з','расшифровать','р','взломать','в']:
            return mode
        print('Введите "зашифровать" или "з" для зашифровки')
        print('Введите "расшифровать" или "р" для расшифровки')
        print('Введите "взломать" или "в" для взлома')
        

def getText():
    print('Введите текст:')
    return input()

def getKey():
    print('Введите ключ шифрования (1-%s):' % (MAX_SIZE_KEY))
    while True:
        key = int(input())
        if (key>=1 and key<=MAX_SIZE_KEY):
            return key
        print('Надо ввести от 1 до %s' % (MAX_SIZE_KEY))

def getTranslate(mode,text,key):
    if mode[0] == 'р':
        key = -key
    
    transl = ''

    for symbol in text:
        symbolIndex = SYMBOLS.find(symbol)

        if symbolIndex == -1:
            transl += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            transl += SYMBOLS[symbolIndex]

    return transl
            
mode = getMode()
text = getText()
if mode[0] != 'в':
    key = getKey()

print('Преобразованный текст:')
if mode[0] != 'в':
    print(getTranslate(mode,text,key))
else:
    for i in range(1,MAX_SIZE_KEY+1):
        print(i,getTranslate('расшифровать',text,i))



        

