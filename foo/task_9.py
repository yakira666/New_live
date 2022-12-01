import math


def square(radius: float) -> float:
    """
     Функция подсчитывает площадь круга, округляя результат до двух знаков после запятой

    :param radius: Радиус круга
    :return: Возращает площадь круга
    """
    res = math.pi * radius ** 2
    return res


# =======================================
def area_of_circle(radius: float) -> float:
    """
     Функция подсчитывает площадь круга, округляя результат до двух знаков после запятой

    :param radius: Радиус круга
    :return: Возращает площадь круга
    """
    PI = 3.14  # константа

    area = PI * radius ** 2
    return area


print(f'{square(float(input("Введите радиус круга: "))):.2f}')
print(f'{area_of_circle(float(input("Введите радиус круга: "))):.2f}')
