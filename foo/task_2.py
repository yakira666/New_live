def multiplication_table():
    for s_num in range(1, 10):
        print(f'\n{"":-^23}\nТаблица умножения на {s_num}\n{"":-^23}')
        for f_num in range(1, 10):
            print(f'{f_num} x {s_num} = {s_num * f_num}')


multiplication_table()
