def library_filling(text: str = "python") -> None:
    # library = []
    # library.append(text)
    """
    Функция наполняет библиотеку слов до тех пор пока не встретиться пустая строка или слово которое уже было и
    выводит на экран количество слов в библиотеке

    :param text: изначальная библиотека слов
    :return: None
    """
    library = [text]
    while word := input("Укажите любое слово: "):

        if word in library:
            print(f'Строка {word} уже присутствует в списке на позиции "{library.index(word)}"')
            break
        library.append(word)
    else:
        print(f"{library}")


if not (line := input("Укажите аргумент (необязательное поле): ")):
    library_filling()
else:
    library_filling(line)
