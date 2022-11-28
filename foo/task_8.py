def sum_nums(num):
    res = (num // 100) + (num % 100) + num
    return res


digit = int(input())
print(sum_nums(digit)) if digit >= 0 else print("Число должно быть трехзначным положительным...")
