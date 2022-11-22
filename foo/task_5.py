num = int(input("Введите целое положительное число: "))


def parity(num):
    if num % 2 == 0:
        print(f'{num} это четное число')
    else:
        print(f'{num} это нечетное число')


parity(num)
