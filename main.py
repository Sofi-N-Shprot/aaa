from math import pow
from unittest import case
print("""Варианты задач:
00 - выход (для всех задач)
1. Перевод числа из десятичной в двоичную СС
2. Перевод из двоичной в десятичную СС
3. Перевод км/ч в м/с
4. Перевод м/с в км/ч
5. Перевод градусов Цельсия в градусы по Фаренгейту
6. Перевод градусов по Фаренгейту в градусы Цельсия""")
while True:
    try:
        num_of_task = int(input("Введите номер задачи (от 0 до 6): "))
        if 0 <= num_of_task <= 6:
            break
        else:
            print("От 0 до 6!")
            continue
    except ValueError:
        print("Число!")


def convert_10_2(num):
    new_num = []
    i = 0
    result = ''
    while num > 0:
        new_num.insert(i, int(num % 2))
        num //= 2
        i += 1
    lst_res = new_num[::-1]
    for j in range(len(lst_res)):
        result += str(lst_res[j])
    print(result)


def convert_2_10(num):
    new_num = []
    l = 0
    res = 0
    while num > 0:
        new_num.append(num % 10)
        num //= 10
        l += 1
    for i in range(l):
        res += new_num[i] * (2 ** i)
    print(res)


def turn_kmh_ms(num):
    result = num / 3.6
    print(round(result, 2), "м/с")


def turn_ms_kmh(num):
    result = num * 3.6
    print(round(result, 2))


def c_to_f(num):
    result = 1.8 * num + 32
    print(round(result, 2))


def f_to_c(num):
    result = (num - 32) / 1.8
    print(round(result, 2))


while True:
    match num_of_task:
        case 0:
            print("Выход")
            exit()
        case 1:
            while True:
                try:
                    n = int(input("Перевод числа из десятичной в двоичную СС. Введите число: "))
                    if n == 0:
                        print("Выход.")
                        exit()
                    if n < 1:
                        print("Число должно быть положительное!")
                        continue
                    if n >= 1:
                        break
                except ValueError:
                    print("Число!")
            convert_10_2(n)
        case 2:
            while True:
                n = str(input("Введите число в двоичной СС: "))
                if not n.isdigit() or "2" in n or "3" in n or "4" in n or "5" in n or "6" in n or "7" in n or "8" in n or "9" in n:
                    print("Только 0 и 1!")
                    continue
                if int(n) == 0:
                    print("Выход")
                    exit()
                else:
                    break
            convert_2_10(int(n))
        case 3:
            while True:
                try:
                    n = int(input("Введите скорость в километрах в час: "))
                    if n == 0:
                        print("Выход.")
                        exit()
                    break
                except ValueError:
                    print("Число!")
            turn_kmh_ms(n)
        case 4:
            while True:
                try:
                    n = int(input("Введите скорость в метрах в секунду: "))
                    if n == 0:
                        print("Выход.")
                        exit()
                    break
                except ValueError:
                    print("Число!")
            turn_ms_kmh(n)
        case 5:
            while True:
                try:
                    n = int(input("Введите градусы в цельсиях: "))
                    if n == 0:
                        print("Выход.")
                        exit()
                    break
                except ValueError:
                    print("Число!")
            c_to_f(n)
        case 6:
            while True:
                try:
                    n = int(input("Введите градусы в фаренгейтах: "))
                    if n == 0:
                        print("Выход.")
                        exit()
                    break
                except ValueError:
                    print("Число!")
            f_to_c(n)
