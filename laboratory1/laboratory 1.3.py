import re

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


x=float_input('Введіть будь-яке число: ')
if x<=1:
    print(0)
elif x>1:
    b=1/(x+6)
    print('Отриманий результат: ' + str(b))