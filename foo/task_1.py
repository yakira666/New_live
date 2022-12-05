def up_text(text: str) -> None:
    """
    Функция меняет регистр на верхний

    :param text: Любой текст
    :return: Возращает текст в вехрнем регистре
    """
    print(f"{text.upper()}")


up_text(input("Введите ваш текст: "))
