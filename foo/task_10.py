def cube_root(digit):
    res = digit ** (1 / 3)
    return res


num = int(input("Введите положительное целое число: "))
print(f'{cube_root(num):.1f}') if num > 0 else print("Число должно быть положительным")
