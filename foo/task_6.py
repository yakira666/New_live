print(f'{"Доступные языки":=^25}\n1.Русский\t2.Английский\n')
language = input("Выберети язык: ")
word = input("Введите слово: ").lower()


def alpha(language, word):
    vowels = "уеоыаэяиёюa"
    vowels_eng = "eiouy"
    consonants = "цкнйгшщзхфвпрлджчсмтб"
    consonants_eng = "bcdfghjklmnpqrstvwxyz"
    counter_v = 0
    counter_c = 0
    if language == "1" and word.isalpha():
        for ch in set(word):
            if ch in vowels:
                counter_v += word.count(ch)
            elif ch in consonants:
                counter_c += word.count(ch)
        print(f'\nКоличество гласных: {counter_v}\nКоличество согласных: {counter_c}')
    elif language == "2" and word.isalpha():
        for ch in set(word):
            if ch in vowels_eng:
                counter_v += word.count(ch)
            elif ch in consonants_eng:
                counter_c += word.count(ch)
        print(f'\nКоличество гласных: {counter_v}\nКоличество согласных: {counter_c}')
    else:
        print("Ошибка...")


alpha(language, word)
