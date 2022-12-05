def library_filling(text: str = "python") -> None:
    """
    Функция наполняет библиотеку слов до тех пор пока не встретиться пустая строка или слово которое уже было

    :param text: изначальная библиотека слов
    :return: возращает количество слов в библиотеке
    """
    library.append(text)
    while (word := input("Укажите любое слово: ")) != "":
        if word not in library:
            library.append(word)
        else:
            print(f'Строка {word} уже присутствует в списке на позиции "{library.index(word)}"')

    print(f"{library}")


library = []
agr = input("Укажите аргумент (необязательное поле): ").strip()
if agr.isalpha():
    library_filling(agr)
else:
    library_filling()
