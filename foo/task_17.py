def external_foo(a: int, b: int) -> int:
    """
    Функция принимает 2 аргумента и передает их внутреней

    :param a: первое целое число
    :param b: второе целое число
    :return: возвращает сумму аргументов c добавлением 10
    """

    def internal_foo() -> int:
        """
        Функция считает сумму аргументов внешней функции

        :return: возращает сумму аргументов
        """
        return a + b

    return internal_foo() + 10


print(external_foo(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
