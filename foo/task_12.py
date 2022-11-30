def is_prime(num: int) -> bool:
    """
    Функция проверяет каким является число: простым или сложным

    :param num: Положительное целое число
    :return: Возвращает булевое значение (True если переданное число является простым, и значение False, если переданное число является сложным)
    """
    for i in range(2, (num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if digit := int(input("Введите положительное целое число: ")) < 0:
    print("Отрицательные целые числа не могут быть простыми!")
elif digit in range(0, 2):
    print("0 и 1 не простые числа")
else:
    print(is_prime(digit))
