def sum_nums(f_num: int, s_num: int):
    """
    Функция считает сумму аргументов

    :param f_num: первое целое число
    :param s_num: второе целое число
    :return: Результат суммы аргументов
    """
    print(text, f_num + s_num)


text = f"\nРезультат первой функции"
first_num = int(input("Введите первое число: ").strip())
second_num = int(input("Введите второе число: ").strip())
sum_nums(first_num, second_num)

text = "Результат функции с новым именем"
rename_foo = sum_nums
rename_foo(first_num, second_num)
