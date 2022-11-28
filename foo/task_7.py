def sum_nums(num):
    print(sum(int(digit) for digit in num.strip().replace(" ", "")))


sum_nums(input("Введите положительное целое число: "))
