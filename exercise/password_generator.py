import random


def show_variant():
    print(
        """Выберите пункты необходимых символов для пароля 
        и введите их через запятую.
        \n1.Прописные буквы\n2.Цифры
        \n3.Строчные буквы\n4.Специальные символы\n""")


def get_choices():
    keys = list(set(int(i) for i in input("Введите пункты: ").strip()
                    if i.isdigit() if int(i) in range(1, 5)))
    return keys


def get_password(keys, length):
    vars = ''
    chars = {
        1: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        2: "1234567890",
        3: "abcdefghijklmnopqrstuvwxyz",
        4: "!@#$%^&*()_",
    }

    for key in keys:
        vars += chars[key]
    return print(f"\nВаш пароль: {''.join(random.choices(vars, k=length))}")


def run():
    show_variant()
    choice = get_choices()

    if choice:
        long_pass = int(input("Введите необходимую длину пароля: "))
        get_password(choice, long_pass)
    else:
        print('\nПопробуйте еще раз выбрать пункты необходимых символов для пароля!')


if __name__ == "__main__":
    run()
