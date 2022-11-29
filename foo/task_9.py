# import math
#
#
# def square(radius):
#     res = math.pi * radius ** 2
#     return res
#
#
# print(f'{square(float(input("Введите радиус круга: " ))):.2f}')

# =======================================
def area_of_circle(radius):
    PI = 3.14  # константа

    area = PI * radius ** 2
    return area


print(f'{area_of_circle(float(input("Введите радиус круга: "))):.2f}')  # Молодц!
