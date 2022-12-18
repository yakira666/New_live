user_1 = [int(elem) for elem in input("Введите сторону противника: ").strip("[] ").replace(",", "").split()]
user_2 = [int(elem) for elem in input("Введите вашу сторону: ").strip("[] ").replace(",", "").split()]


def is_defended(attackers: list, defenders: list) -> bool:
    """
    Функция принимает 2 списка и сравнивает их элементы(солдат) по величине(силе атаки)

    :param attackers: Входящий отряд противника
    :param defenders: Ваш входящий отряд
    :return: bool
    """
    attack_counter = 0
    def_counter = 0

    long_min_list = min(len(attackers), len(defenders))
    if len(attackers) > len(defenders):
        attack_counter += len(attackers) - len(defenders)
    else:
        def_counter += len(defenders) - len(attackers)

    for i in range(long_min_list):
        if defenders[i] > attackers[i]:
            def_counter += 1
        elif attackers[i] > defenders[i]:
            attack_counter += 1
        else:
            continue

    if def_counter > attack_counter:
        return True
    elif attack_counter > def_counter:
        return False
    elif def_counter == attack_counter:
        if sum(defenders) == sum(attackers):
            return True
        else:
            return False


print(is_defended(user_1, user_2))
