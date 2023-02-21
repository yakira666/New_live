from question import Question

import json
import random


def reader_json(filename: str) -> list[dict]:
    """Принимает и обрабатывает json файлы"""
    with open(file=filename, mode="r", encoding="UTF-8") as jf:
        context: list[dict] = json.load(jf)
        return context


def game():
    print("Программа: Игра начинается!".center(60, "#"))

    context = reader_json("questions.json")  # считываем данные из json
    random.shuffle(context)  # перемешивание вопросов

    total_points = 0  # общее кол-во баллов
    count_correct_ans = 0  # кол-во правильных ответов
    for que in context:
        q_text = que["q"]
        lvl = int(que["d"])

        print(Question.build_question(q_text, lvl))  # вызов метода, построение вопроса

        user_input = input("Пользователь (для выхода quit): ")
        if user_input.lower() == "quit":
            break
        obj1 = Question(q_text, lvl, user_input, que["a"])  # создание объекта

        if obj1.is_correct():  # вывод, исходя от ответа пользователя
            print(obj1.build_positive_feedback(), end='\n\n')
            count_correct_ans += 1
            total_points += obj1.get_point()
        else:
            print(obj1.build_negative_feedback())
    print(f"Отвечено {count_correct_ans} вопроса из {len(context)}"
          f"\nНабрано {total_points} баллов")

    print("До новых встреч!")


if __name__ == "__main__":
    game()
