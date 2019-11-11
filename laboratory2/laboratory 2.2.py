import re

restart = 'a'

while restart == 'a':
    value = 1
    sum = 0
    count = 0


    def float_input(message):
        flag = False
        while not flag:
            a = input(message)
            if bool(re.match('^[+-]{0,1}[0-9]{1,}(\.[0-9]{1,})?$', a)):
                flag = True
                a = float(a)
            else:
                print("Сталася помилка. Спробуйте ще раз")
        return a

    while value != 0:
        value = float_input("Введіть число: ")

        sum = sum + value
        count = count+1

    print("Сума =",sum)
    print("Кількість цифр =",count)
    print("Середнє арифметичне =", round(sum/count,4))
    restart = input("Для повторного запуску програми введіть 'а' або для виходу з програми - будь-яку іншу клавішу\n")

print('Робота з програмою завершена.')