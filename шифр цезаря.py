alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_EUa = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavit_RUa = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

n = int(input("Для шифрования сообщения введите 1, Для дешифровки - 2:  "))
lang = input("Выберите язык ru/eu: ")
message = input("Введите сообщение: ")

# Проверка на наличие латинских символов в строке
def Any_Latin_Letters(message):
    for x in message:
        if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
            return True
    return False

# Проверка на ошибку
if lang == "ru" and Any_Latin_Letters(message) == True:
    print("Выберите другой язык.")
    exit()
else: 
    pass

if lang == "eu" and Any_Latin_Letters(message) == False:
    print("Выберите другой язык.")
    exit()
else: 
    pass


step = int(input("Введите шаг шифровки: "))
result = ""


if n == 1:
    if lang == "ru":
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



    if lang == "eu":
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
    if lang == "ru":
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
        
    
    if lang == "eu":
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
