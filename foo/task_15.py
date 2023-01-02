def show_employee(name: str, salary: int = 50_000):
    """
    Функция выводит имя и зарплату сотрудника

    :param name: имя сотрудника
    :param salary: зарплата сотрудника, по умолчанию 50 000
    :return: None
    """

    # print(f"Имя: {name}\nЗарплата: {salary / 1000:.3f}₽")  # зачем делишь на 1000 и рубля?

    print(f"Имя: {name}\nЗарплата: {salary:,}{chr(8381)}")


# Молодец!
user_name = input("Введите имя (обязательное поле): ").strip().capitalize()
user_salary = input("Укажите зарплату (необязательное поле): ")

if user_salary.isdigit():
    show_employee(user_name, int(user_salary))
else:
    show_employee(user_name)
