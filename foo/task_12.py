def is_simple(num):
    for i in range(2, (num // 2) + 1):  # я не согласен с условием range(2, (num // 2) + 1), почему так?
        if num % i == 0:
            return False
    return True


# Здесь можно улучшить условие, используй моржовый оператор
digit = int(input("Введите положительное целое число: "))
if digit < 0:
    print("Отрицательные целые числа не могут быть простыми!")
elif digit in range(0, 2):
    print("0 и 1 не простые числа")
else:
    print(is_simple(digit))
