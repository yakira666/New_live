def find_it(seq: list) -> int:
    unique_numbers = set(seq)

    for n in unique_numbers:
        if seq.count(n) % 2 != 0:
            return n


if __name__ == '__main__':
    print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))  # 5

