def nums(first_num, second_num):
    prod = first_num * second_num

    # res_2 = first_num + second_num  # зачем лишняя переменная :)

    if prod <= 1000:
        return prod

    # также блок else не понадобится, почему? Если условие будет истинным первый return сработает и функция
    # завершает свою работу, иначе просто выполнится то что после if

    return first_num + second_num


print(nums(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
