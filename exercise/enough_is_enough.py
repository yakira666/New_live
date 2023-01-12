def delete_nth(order: list, max_e: int) -> list:
    result = []
    for n in order:
        if result.count(n) < max_e:
            result.append(n)

    return result


if __name__ == '__main__':
    print(delete_nth([20, 37, 20, 21], 1))  # [20, 37, 21]
    print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))  # [1, 1, 3, 3, 7, 2, 2, 2]
