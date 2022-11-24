def parity(n):
    if n % 2 == 0:
        print(f'{n} это четное число')
    else:
        print(f'{n} это нечетное число')


num = int(input("Введите целое положительное число: "))
parity(num)

# parity(int(input("Введите целое положительное число: ")))
