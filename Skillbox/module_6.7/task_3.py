print('Задача 3. Слишком большие числа')

num = int(input("Введите число: "))
count = 0

while num:
    num = num // 10
    count += 1
print("Колличество цифр в числе:", count)

# У неудачливого бухгалтера всё опять идёт наперекосяк: ему приносят такие большие счета, что числа не помещаются на бумаге.

# Напишите программу, которая считала бы для него, сколько цифр во вводимом числе. Обратите внимание, что число 0 имеет одну цифру.

# Пример:
# Введите число: 567
# Ответ: 3

# Введите число: 1203
# Ответ: 4
