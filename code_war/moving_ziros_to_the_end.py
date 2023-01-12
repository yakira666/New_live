def move_zeros(lst):
    num = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[num], lst[i] = lst[i], lst[num]
            num += 1
    return lst


# def move_zeros(lst):
#     for i in range(len(lst)):
#         if lst[i] == 0:
#             lst.remove(lst[i])
#             lst.append(0)
#     return lst


print(move_zeros([2, 0, 0, 0, 0, 0, 0, 0, 0, 1]))