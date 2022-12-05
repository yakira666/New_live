def show_employee(name: str, salary=50000):
    """
    Функция выводит имя и зарплату сотрудника

    :param name: имя сотрудника
    :param salary: зарплата сотрудника
    :return: функция возращает имя и зарплату сотрудника
    """
    print(f"Имя: {name}\nЗарплата: {salary / 1000:.3f}₽")


user_name = input("Введите имя (обязательное поле): ").strip().capitalize()
user_salary = input("Укажите зарплату (необязательное поле): ")
if user_salary.isdigit():
    show_employee(user_name, int(user_salary))
else:
    show_employee(user_name)
