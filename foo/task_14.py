def math_operations(f_num: int, s_num: int):
    """
    Функция вычисляет сумму и разность полученных целых чисел

    :param f_num: первое целое число
    :param s_num: второе целое число
    :return: Возращает сумму и разность целых чисел
    """

    return f_num + s_num, f_num - s_num


# math_operations = lambda x, y: f'\nsumma = {x}\ndifference = {y}'

print(
    f'\nsumma = {(math_operations(fnum := int(input("Введите первое целое число: ").strip()), snum := int(input("Введите второе целое число: ").strip())))[0]}'
    f'\ndifference = {(math_operations(fnum, snum))[1]}'
)
