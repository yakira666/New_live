def count_smileys(arr) -> int:
    nose = "-~"  # 1
    mouth = ")D"  # 1
    smileys = []  # 1
    eyes = ":;"  # 1
    counter = 0  # 1
    # 5

    # 6
    for e in eyes:  # n^3
        for n in nose:
            for m in mouth:
                smileys.append(e + n + m)  # 1
                smileys.append(e + m)  # 1
    # n^3 + 2

    for el in arr:  # n
        if el in smileys:  # 1
            counter += 1  # 1
    # n + 2

    # в худшем случае n^3 + n  #
    return counter


entry_arr = [';]', ':[', ';*', ':$', ';-D']
# entry_arr = input().strip(" []").replace(" ", "").replace("\'", "").split(",")
print(count_smileys(entry_arr))
