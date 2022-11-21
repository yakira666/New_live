num = int(input("Введите целое положительное число: "))


def factorial(num):
    if num < 0:
        print("Факториал отрицательного числа невозможен...")
    elif num > 0:
        s = 1
        for s_num in range(1, num + 1):
            s = s * s_num
        print(f'Факториал числа {num} равен {s:,.0f}')
    else:
        print(0)


factorial(num)
