class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> str:
        """Метод определяет можно ли построить треугольник"""

        if (self.a > 0) and (self.b > 0) and (self.c > 0):
            return "Ура можно построить треугольник!"
        elif (self.a < 0) or (self.b < 0) or (self.c < 0):
            return "С отрицательными числами ничего не выйдет"
        else:
            return "Жаль, но из этого треугольник не сделать"


se = TriangleChecker(1, 0, 3)
se1 = TriangleChecker(2, 5, 3)
try:
    print(se.is_triangle())
    print(se1.is_triangle())
except (ValueError, TypeError):
    print("Нужно вводить только числа!")
