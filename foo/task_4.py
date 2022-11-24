num = int(input("Введите целое положительное число: "))


def factorial(number):
    if number < 0:
        print("Факториал отрицательного числа невозможен...")

    elif number == 0:
        print(0)

    else:
        prod = 1
        for number in range(1, number + 1):
            prod = prod * number
        print(f'Факториал числа {number:d} равен {prod:,d}')


factorial(num)
