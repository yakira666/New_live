print('Задача 1. Калькулятор опыта')

exp_point = int(input("Введите количество опыта: "))
yu_lvl = "Ваш уровень:"

if exp_point < 1000:
    print(yu_lvl, 1)
elif 1000 <= exp_point < 2500:
    print(yu_lvl, 2)
elif 2500 <= exp_point < 5000:
    print(yu_lvl, 3)
else:
    print(yu_lvl, 4)

# В свободное время Вася любит играть в компьютерные игры. Однажды у него появилась классная идея для сюжета игры. Чтобы воплотить её в жизнь, он начал изучать геймдизайн. Создавать игру он начал с главного героя и его системы прокачки.

# Напишите программу, которая определяет уровень персонажа в компьютерной игре. Пользователь вводит число «очков опыта», а программа вычисляет уровень. Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.

# Пример:
# Введите количество опыта: 6000
# Ваш уровень: 4

# Пример 2:
# Введите количество опыта: 2000
# Ваш уровень: 2
