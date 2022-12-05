def external_foo(arg_1: int, arg_2: int) -> int:
    """
    Функция принимает 2 аргумента и передает их внутреней

    :param arg_1: первое целое число
    :param arg_2: второе целое число
    :return: возвращает сумму аргументов c добавлением 10
    """
    def internal_foo(arg_1_2: int, arg_2_2: int) -> int:
        """
        Функция считает сумму полученных аргументов

        :param arg_1_2: первое целое число
        :param arg_2_2: второе целое число
        :return: возращает сумму аргументов
        """
        return arg_1_2 + arg_2_2
    return internal_foo(arg_1, arg_2) + 10


print(external_foo(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
