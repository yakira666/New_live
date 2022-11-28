def is_simple(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


digit = int(input("Введите положительное целое число: "))
if digit == 0 or digit == 1:
    print("0 и 1 не простые числа")
elif digit < 0:
    print("Отрицательные целые числа не могут быть простыми!")
else:
    print(is_simple(digit))
