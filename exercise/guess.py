import random
from colorama import Fore, Style, Back, init

init(autoreset=True)

guess = random.choice(range(1, 101))  # рандомное число

print(guess)

print(f' {Back.WHITE}{Fore.RED}"Угадай число!"{Style.RESET_ALL} '.center(50, '#'))

attempt = 5  # количество попыток
while (n := int(input('Введите число в диапазоне от 1 до 100 (0 для выхода): '))):

    if n in range(1, 101):
        if n > guess:
            print('Загаданное число меньше')
        elif n < guess:
            print('Загаданное число больше')
        else:
            print('ПОБЕДА!')
            break
        attempt -= 1
    else:
        print('Введите число в диапазоне от 1 до 100...')
        attempt -= 1
    
    if attempt <= 0:
        print(f'Вы проиграли, попробуйте ещё раз!\nЗагаданное число -> {guess}')
        break
else:
    print('До новых встреч!')
