def number_of_signs(sentence: str) -> int:
    """
    Функция считает количество символов во входящей строке без учета пробелов

    :param sentence: исходный текст (предложение)
    :return: возращает количество символов без учета пробелов
    """
    return int(len(sentence))


print(
    f'Количество символов в предложении: {number_of_signs(input("Введите предложение: ").strip().replace(" ", ""))}\n',
    number_of_signs.__doc__)
