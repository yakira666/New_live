import random


def password(w, length):
    a = ''
    p = {
        1: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        2: "1234567890",
        3: "abcdefghijklmnopqrstuvwxyz",
        4: "!@#$%^&*()_",

    }

    for i in w:
        a += p[i]
    return print(f"\nВаш пароль: "
                 f"{''.join(random.choice(a) for _ in range(length))}")


if __name__ == "__main__":
    key_security = list(
        set(int(i) for i in input(f"Выберите пункты необходимых символов для пароля и введите их через запятую. "
                                  f"\n1.Прописные буквы "
                                  f"\n2.Цифры "
                                  f"\n3.Строчные буквы "
                                  f"\n4.Специальные символы\n\nВведите пункты : ").strip() if i.isdigit()))
    long_pass = int(input("Введите необходимую длину пароля: "))

    if max(key_security) < 5:
        password(key_security, long_pass)
    else:
        print('\nПопробуйте еще раз выбрать пункты необходимых символов для пароля!')
