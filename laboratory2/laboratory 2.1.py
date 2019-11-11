import re

restart = 'a'
print('Біловодський Іван, КМ-94 \nВаріант №4')

def float_input(message):
    flag = False
    while not flag:
        a = input(message)
        if bool(re.match('^[+-]{0,1}[0-9]{1,}(\.[0-9]{1,})?$',a)):
            flag = True
            a = float(a)
        else:
            print("Сталася помилка. Спробуйте ще раз")
    return a

def int_input(message):
    flag = False
    while not flag:
        a = input(message)
        if bool(re.match('^[+]{0,1}[0-9]{1,}$',a)):
            flag = True
            a = int(a)
        else:
            print("Сталася помилка. Спробуйте ще раз")
    return a

while restart == 'a':
    n = int_input("Введіть кількість повторів: ")
    x = float_input("Введіть число: ")

    sum = 0

    for i in range(1, n+1):
        sum = sum + (x + i) / i

    print("Значення суми: ", round(sum, 4))
    restart = input("Для повторного запуску програми введіть 'a' або для виходу з програми - будь-яку іншу клавішу\n")

print('Робота з програмою завершена.')