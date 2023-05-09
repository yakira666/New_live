print('Задача 7. Метод бутерброда')

res = ""
data = input("Введите зашифрованное сообщение: ")

for char in range(0, len(data), 2):
    res += data[char]

for char in range(1, len(data), 2):
    res += data[-char]

print(res)
# В секретном агентстве Super-Secret-no решили использовать «метод бутерброда» для шифрования переписки своих сотрудников. Сначала буквы слова нумеруются в таком порядке: первая буква получает номер 1, последняя буква — номер 2, вторая — номер 3, предпоследняя — номер 4, потом третья… и так для всех букв (см. рисунок). Затем все буквы записываются в шифр в порядке своих номеров.

# Например, слово «sandwich» зашифруется в «shacnidw».
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.

# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
# Шифр:  | s | h | a | c | n | i | d | w |
