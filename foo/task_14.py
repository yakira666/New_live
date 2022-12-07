def calc_subtraction_addition(f_num: int, s_num: int):
    """
    Функция вычисляет сумму и разность полученных целых чисел

    :param f_num: первое целое число
    :param s_num: второе целое число
    :return: Возращает сумму и разность целых чисел
    """

    return f_num + s_num, f_num - s_num


# calc_subtraction_addition = lambda x, y: f'\nsumma = {x}\ndifference = {y}'

# print(
#     f'\nsumma = {(calc_subtraction_addition(fnum := int(input("Введите первое целое число: ").strip()), snum := int(input("Введите второе целое число: ").strip())))[0]}'
#     f'\ndifference = {(calc_subtraction_addition(fnum, snum))[1]}'
# )

# Без проверки я был уверен, что этот код будет работать, но посмотри какой он сложный, согласен?

# здесь можно было сделать хитрый ход

num_1 = int(input("Введите первое целое число: "))
num_2 = int(input("Введите второе целое число: "))

summa, difference = calc_subtraction_addition(num_1, num_2)
print(f'\n{summa = }\n{difference = }')  # :)
