def sum_nums(f_num: int, s_num: int) -> None:
    """
    Функция считает сумму аргументов и выводит на экран

    :param f_num: первое целое число
    :param s_num: второе целое число
    :return:
    """
    print(f_num + s_num)


first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

# вызов функции с использованием исходного имени
print('\nРезультат первой функции: ', end='')
sum_nums(first_num, second_num)

# назначить новое имя
new_sum_nums = sum_nums

# вызов функции с использованием нового имени
print('Результат функции с новым именем: ', end='')
new_sum_nums(first_num, second_num)
