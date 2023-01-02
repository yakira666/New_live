# def several_arguments(*args):
#     """
#     Функция разбивает текст по пробелам и выводит каждый элемент на новой строке
#
#     :param args: переменное количество аргументов
#     :return: None
#     """
#     for item in args[0]:
#         print(item)
#
#
# if s := input("Введите аргументы через пробел: ").strip().split():
#     several_arguments(s)
# else:
#     print("Ошибка: Введите что нибудь...")


# второе решение


def several_arguments(*args):
    """
    Функция разбивает текст по пробелам и выводит каждый элемент на новой строке

    :param args: переменное количество аргументов
    :return: None
    """
    for item in args:
        print(item)


if not (line := input('Введите аргументы через пробел: ').strip().split()):
    print('Ошибка: Введите что-нибудь...')
else:

    several_arguments(*line)
