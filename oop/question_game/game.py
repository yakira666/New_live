# from question import Question

import json
import random


def reader_json(test: int | str | float = 1):
    """Принимает и обрабатывает json файлы"""

    with open("questions.json", "r", encoding="UTF-8") as jf:
        text = json.load(jf)
        random.shuffle(text)
        programm = "Программа: "
        all_points = 0
        count_true_answer = 0
        print("Игра началась!")
        for el in text:
            quest = el["q"]
            lvl = int(el["d"])
            answer = el["a"]
            print(f'{programm}Вопрос: {quest}\n{programm}Сложность: {lvl}/5')
            user_anser = input("Пользователь: ")
            if user_anser == answer:
                print(f'{programm}Ответ верный, получено {lvl * 10} баллов')
                all_points += lvl * 10
                count_true_answer += 1
            else:
                print(f'{programm}Ответ неверный, Верный ответ - {answer}')
    print(f'{programm}Вот и все!\n{programm}Отвечено на {count_true_answer} вопроса из {len(text)}\n{programm}Набрано: {all_points} баллов')

def main():
    """Создать 5 экз. класса Question, добавить в список далее перемешать их с помощью шафла"""

    pass


if __name__ == "__main__":
    main()
    reader_json()
