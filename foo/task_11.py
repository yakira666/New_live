def nums(first_num: int, second_num: int) -> int:
    """
    Функция, принимает два целых числа и возвращает их произведение, если произведение меньше или
    равно 1000, в противном случае возвращает их сумму.

    :param first_num: Первое целое число
    :param second_num: Второе целое число
    :return: Возвращает их произведение, если произведение меньше или равно 1000, в противном случае возвращает их сумму
    .
    """
    prod = first_num * second_num

    if prod <= 1000:
        return prod

    return first_num + second_num


print(nums(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
