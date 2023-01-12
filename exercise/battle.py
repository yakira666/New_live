def is_defended(attackers: list, defenders: list) -> bool:
    """
    Функция принимает 2 списка и сравнивает их элементы(солдат) по величине(силе атаки)

    :param attackers: Входящий отряд противника
    :param defenders: Ваш входящий отряд
    :return: bool
    """
    attack_counter = 0
    def_counter = 0

    size_attackers = len(attackers)  # кол-во атакующих
    size_defenders = len(defenders)  # кол-во защитников

    if size_attackers > size_defenders:
        attack_counter += size_attackers - size_defenders

    elif size_attackers < size_defenders:
        def_counter += size_defenders - size_attackers

    for i in range(min(size_attackers, size_defenders)):
        if defenders[i] > attackers[i]:
            def_counter += 1
        elif attackers[i] > defenders[i]:
            attack_counter += 1

    if def_counter > attack_counter:
        return True
    elif attack_counter > def_counter:
        return False
    else:
        attack_damage = sum(attackers)
        defenders_damage = sum(defenders)

        if defenders_damage > attack_damage:
            return True
        elif defenders_damage < attack_damage:
            return False

        return True


if __name__ == '__main__':
    # user_1 = [int(elem) for elem in input("Введите сторону противника: ").strip("[] ").replace(",", "").split()]
    # user_2 = [int(elem) for elem in input("Введите вашу сторону: ").strip("[] ").replace(",", "").split()]
    # print(is_defended(user_1, user_2))

    # is_defended([2, 9, 9, 7], [1, 1, 3, 8])
    # is_defended([1, 3, 5, 7], [2, 4, 6, 8])
    # is_defended([10, 10, 1, 1], [4, 4, 7, 7])
    # is_defended([], [1, 2, 3])
    # is_defended([1, 2, 3], [])
    print(is_defended([30, 13, 14, 16, 29, 13, 10, 2], [34, 11, 26, 36, 17, 14]))  # True

# a = 1 + 1 + 1
# d = 1 + 1 + 1 + 1 + 1
# e
