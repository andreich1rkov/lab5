alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_EUa = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_RUa = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Выбор режима
while True:
    try:
        n = int(input("Для шифрования сообщения введите 1, Для дешифровки - 2:  "))
        if n not in range(1,3):
            raise ValueError
        break
    except ValueError:
        print("Ошибка. Для шифрования сообщения введите 1, Для дешифровки - 2:  ")

# Выбр языка
while True:
    try:
        lang = int(input("Выберите язык Для RU введите 1, для EU введите 2: "))
        if lang not in range(1,3):
            raise ValueError
        break
    except ValueError:
        print("Ошибка. Для шифрования сообщения введите 1, Для дешифровки - 2:  ")

# Ввод сообщения
message = input("Введите сообщение: ")

# Проверка на наличие латинских символов в строке
def Any_Latin_Letters(message):
    for x in message:
        if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
            return True
    return False

# Проверка на ошибку
if lang == 1 and Any_Latin_Letters(message) == True:
    print("Выберите другой язык.")
    exit()
else: 
    pass

if lang == 2 and Any_Latin_Letters(message) == False:
    print("Выберите другой язык.")
    exit()
else: 
    pass

# Ввод шага шифрования
while True:
    try:
        step = int(input("Введите шаг шифровки: "))
        if step == 0:
            raise ValueError
        break
    except ValueError:
        print("Ошибка. Для шага шифровки введите целое число.")
if step < 0:
    step = abs(step)

result = ""


if n == 1:
    if lang == 1:
        for i in message:
            if i.isupper():
                mesto = alfavit_RU.find(i)
                new_mesto = mesto + step
                if i in alfavit_RU:
                    result += alfavit_RU[new_mesto]
            elif i.islower():
                mesto = alfavit_RUa.find(i)
                new_mesto = mesto + step
                if i in alfavit_RUa:
                    result += alfavit_RUa[new_mesto]
            else:
                result += i



    if lang == 2:
        for i in message:
            if i.isupper():
                mesto = alfavit_EU.find(i)
                new_mesto = mesto + step
                if i in alfavit_EU:
                    result += alfavit_EU[new_mesto]
            elif i.islower():
                mesto = alfavit_EUa.find(i)
                new_mesto = mesto + step
                if i in alfavit_EUa:
                    result += alfavit_EUa[new_mesto]
            else:
                result += i


if n == 2:
    if lang == 1:
        for i in message:
            if i.isupper():
                mesto = alfavit_RU.find(i)
                new_mesto = mesto - step
                if i in alfavit_RU:
                     result += alfavit_RU[new_mesto]
            elif i.islower():
                mesto = alfavit_RUa.find(i)
                new_mesto = mesto - step
                if i in alfavit_RUa:
                    result += alfavit_RUa[new_mesto]
            else:
                    result += i
        
    
    if lang == 2:
         for i in message:
            if i.isupper():
                mesto = alfavit_EU.find(i)
                new_mesto = mesto - step
                if i in alfavit_EU:
                    result += alfavit_EU[new_mesto]
            elif i.islower():
                mesto = alfavit_EUa.find(i)
                new_mesto = mesto - step
                if i in alfavit_EUa:
                    result += alfavit_EUa[new_mesto]
            else:
                result += i

print("Результат: ", result)
