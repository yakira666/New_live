def findUniq(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if str(arr[i]).strip() == str(arr[j]).strip() and i != j:
                break
        else:
            return arr[i]


if __name__ == '__main__':
    # Original Kata: https://www.codewars.com/kata/585d7d5adb20cf33cb000235/

    read_values = [
        [1, 1, 1, 2, 1, 1],  # 2
        [0, 0, 0.55, 0, 0],  # 0.55
        [3, '10', 3, 3, 3],  # 10
        [1, 1, 1, 2, 1, 1],
        [4, 4, 'foo', 4],
    ]

    for item in read_values:
        print(findUniq(item))
