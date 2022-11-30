def welcome(name: str) -> str:
    """
    Функция приветствует полученного пользователя

    :param name: Имя пользователя
    :return: Возвращает приветствие пользователя
    """
    print(f"Привет, {name.capitalize()}!")


welcome(input("Введите ваше имя: "))
