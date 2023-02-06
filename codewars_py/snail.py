def snail(snail_map):
    snail_list = []
    try:
        snail_list.extend(snail_map[0])
        del snail_map[0]

        for i in snail_map:
            snail_list.append(i[-1])
            del i[-1]

        snail_list.extend(reversed(snail_map[-1]))
        del snail_map[-1]

        for i in reversed(snail_map):
            snail_list.append(i[0])
            del i[0]

        if len(snail_map) > 1:
            snail_list.extend(snail(snail_map))
        elif len(snail_map) == 1:
            snail_list.extend(snail_map[0])
        return snail_list

    except IndexError:
        return snail_list


if __name__ == '__main__':
    # Original kata https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
    array = [[1, 2, 3, 5, 6],
             [17, 18, 19, 20, 7],
             [16, 25, 26, 21, 8],
             [15, 24, 23, 22, 9],
             [14, 13, 12, 11, 10]]
    print(snail(array))
    array = [[1, 2],
             [3, 4]]
    print(snail(array))
