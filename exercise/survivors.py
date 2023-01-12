def is_defended(attackers, defenders):
    if not attackers:
        return True

    if not defenders:
        return False

    survivors_attack = 0  # кол-во выживних у атакующих
    survivors_defender = 0  # кол-во выживних у обороняющихся

    damage_attack = sum(attackers)  # кол-во силы у атакующих
    damage_defender = sum(defenders)  # кол-во силы у обороняющихся

    length_attackers = len(attackers)
    length_defenders = len(defenders)

    if length_attackers > length_defenders:
        survivors_attack += length_attackers - length_defenders
    elif length_attackers < length_defenders:
        survivors_defender += length_defenders - length_attackers

    arrays = tuple(zip(attackers, defenders))

    for attack, defender in arrays:
        if attack > defender:
            survivors_attack += 1

        elif attack < defender:
            survivors_defender += 1

    if survivors_attack > survivors_defender:
        return False
    elif survivors_attack < survivors_defender:
        return True
    else:
        if damage_attack > damage_defender:
            return False
        elif damage_attack < damage_defender:
            return True

        return True
