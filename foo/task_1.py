def up_text(text: str) -> None:
    """
    Функция меняет регистр на верхний и выводит текст

    :param text: Любой текст
    :return: None
    """
    print(f"{text.upper()}")


up_text(input("Введите ваш текст: "))
