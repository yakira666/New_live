num = int(input("Введите целое положительное число: "))


def factorial(num):
    if num < 0:
        print("Факториал отрицательного числа невозможен...")

    # худший случай всегда лучше написать первым
    elif num == 0:
        print(0)

    else:
        prod = 1
        for n in range(1, num + 1):
            prod = prod * n
        print(f'Факториал числа {num:d} равен {prod:,d}')  # у нас целое число, поэтому вместо 0.f используется d


factorial(num)
