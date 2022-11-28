def nums(fnum, snum):
    res_1 = fnum * snum
    res_2 = fnum + snum
    if res_1 <= 1000:
        return res_1
    else:
        return res_2


print(nums(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
