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

a=float_input('Введіть перше число: ')
b=float_input('Введіть друге число(яке не дорівнює першому): ')
while a == b:
    print("Числа повинні бути різними. Спробуйте ще раз")
    b = float_input('Введіть друге число(яке не дорівнює першому): ')

if a>b:
    c=(a+b)/2
    print('Якщо перше число більше другого, то: ' + str(c))
if a<b:
    c=2*a*b
    print('Якщо перше число менше другого, то: ' + str(c))





