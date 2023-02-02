def fact(n):
    """Рекурсивная функция"""
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    read_values = [1, 2, 3, 4, 6, 7, 8, 9, 10, 996]
    for x in read_values:
        print(fact(x))
