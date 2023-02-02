def cakes(recipe, available):
    l = []
    recipe_ingr = recipe  # Создаем копии
    available_ing = available  # Создаем копии для работы
    
    # Проверяем на разницу ключей и дополняем словари
    if len(recipe_ingr.keys()) < len(available_ing.keys()):  
        for k in available_ing:
            if k not in recipe_ingr:
                recipe_ingr |= {k: 0}

        
    elif len(recipe_ingr.keys()) > len(available_ing.keys()):
        for k in recipe_ingr:
            if k not in available_ing:
                available_ing |= {k: 0}
                

    # Основной блок функции (вычисления)
    for k in recipe_ingr:
        a = int(available_ing.get(k))
        r = int(recipe_ingr.get(k))

        if (a == 0) and (r > 0):
            return 0
        elif (int(r) == 0) and (int(a) > 0):
            l.append(a)
        else:
            l.append(int(a // r))

    return min(l)