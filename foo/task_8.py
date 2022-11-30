def sum_nums(num: int) -> int:
    """
    Функция подсчитывает сумму 3 числе 3-х значного числа

    :param num: Целое трехзначное положительное число
    :return: Возращает результат суммы 3-х чисел полученного числа
    """
    res = (num // 100) + (num % 100) + num
    return res


print(sum_nums(digit)) if (digit := int(input())) >= 0 and len(str(digit)) == 3 else print(
    "Число должно быть трехзначным положительным...")
