num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

if num_1 >= num_2:
    print(f'Разность: {num_1-num_2}\nИгрок платит')
else:
    print(f"Сумма: {num_2+num_1}\nВладелец платит")
print("Игра окончена")

"""
Задача 6. Игра в кубики
Что нужно сделать

Вася понимает, как важен отдых после тяжёлого рабочего дня, поэтому часто ходит в местный бар с друзьями. Владелец бара любит азартные игры и иногда предлагает посетителям с ним сыграть. Вася избегает азартные игры, но предложил владельцу купить у него программу для расчёта результатов игры, которую можно выводить на экраны бара.

Напишите программу: на вход в неё подаётся два числа. Если первое число больше или равно второму, то нужно вывести на экран их разность и отдельной строкой: «Игрок платит». В противном случае, вывести их сумму и отдельной строкой: «Владелец платит». Последней строкой на экран должна быть выведена фраза: «Игра окончена».



Пример:

Кубик Кости: 3

Кубик владельца: 4

Сумма: 7

Владелец платит

Игра окончена
"""
