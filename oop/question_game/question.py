class Question:
    """Базовый класс"""

    # Инициализатор (конструктор)
    def __init__(self,
                 que_text: str,
                 level: int,
                 user_ans: str,
                 correct_ans: str,
                 points: int = 10):
        self.que = que_text
        self.level = level
        self.user_ans = user_ans
        self.correct_ans = correct_ans
        self.points = self.level * points

    def get_point(self) -> int:  # геттер
        """Возвращает количество баллов"""
        return self.points

    def is_correct(self) -> bool:
        """Проверяет ответ пользователя, если совподает с
        правильном ответом возвращает True, иначе False"""

        # if self.user_ans == self.correct_ans:
        #     return True
        # return False
        return self.user_ans == self.correct_ans

    @staticmethod  # это наши обычные функции
    def build_question(q_text, lvl) -> str:
        """Возвращает вопрос в понятном виде"""
        return "Вопрос: {0}\nСложность: {1}/5".format(q_text, lvl)

    def build_positive_feedback(self):
        """Сгенерирует вывод для правильного ответа"""
        # return f"Ответ верный, получено {self.points} баллов"
        return f"Ответ верный, получено {self.get_point()} баллов"

    def build_negative_feedback(self):
        """Сгенерирует вывод для неправильного ответа"""
        return f"Ответ неверный, верный ответ {self.correct_ans}"


if __name__ == "__main__":
    print("Программа: Игра начинается!")

    # example: from json file
    q = "Два плюс два сколько?"
    d = "2"
    a = "4"

    print(f"Программа: Вопрос: {q}\n"
          f"Программа: Сложность: {d}/5")

    user_input = input("Пользователь: ")
    obj1 = Question(q, int(d), user_input, a)
    print(obj1.build_question())

    if obj1.is_correct():
        print(obj1.build_positive_feedback())
    else:
        print(obj1.build_negative_feedback())
