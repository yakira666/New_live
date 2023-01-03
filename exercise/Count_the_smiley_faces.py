def count_smileys(arr) -> int:
    nose = "-~"
    mouth = ")D"
    smileys = []
    eyes = ":;"
    counter = 0

    for e in eyes:
        for n in nose:
            for m in mouth:
                smileys.append(e + n + m)
                smileys.append(e + m)

    for el in arr:
        if el in smileys:
            counter += 1
    return counter


entry_arr = [';]', ':[', ';*', ':$', ';-D']
# entry_arr = input().strip(" []").replace(" ", "").replace("\'", "").split(",")
print(count_smileys(entry_arr))
