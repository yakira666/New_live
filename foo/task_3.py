def welcome(name: str) -> None:
    """
    Функция привествует полученного пользователя и текст выводит на экран

    :param name: Имя пользователя
    :return: None
    """
    print(f"Привет, {name.capitalize()}!")


welcome(input("Введите ваше имя: "))
