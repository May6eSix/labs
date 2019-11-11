import re

print('Варіант 4, обчислення ')
print('Іван Біловодський, КМ-94')

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


c=float_input('Введіть перше число: ')
c=c*2
print(c)
d=float_input('Введіть друге число: ')
d=d-3
print(d)
f=float_input('Введіть третє число: ')
f=f**2
print(f)
e=c+d+f
print('Отриманий результат: '+str(e))

