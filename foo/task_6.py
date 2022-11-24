def count_vowels_and_consonants(word, vowels):
    counter_v = 0
    counter_c = 0
    for ch in word.lower().strip():
        if ch in vowels.lower().strip():
            counter_v += 1
        else:
            counter_c += 1

    print(f'\nКоличество гласных: {counter_v}\nКоличество согласных: {counter_c}')


print(f'{"Доступные языки":=^25}\n1.Русский\t2.Английский\n')

lang = int(input("Выберети язык: "))
line = input("Введите слово: ")

choice_lang = {
    1: "уеоыаэяиёю",
    2: "eiaouy",
}

if lang in choice_lang:
    vow = choice_lang[lang]
    count_vowels_and_consonants(line, vow)
else:
    print("Ошибка...")
