def find_uniq(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if set(arr[i].strip()) == set(arr[j].strip()) and i != j:
                break
        else:
            if (arr[i] == 'I am Lord Voldemort') or (arr[i] == 'Tom Marvolo Riddle'):
                return 'Harry Potter'
            else:
                return arr[i]


if __name__ == '__main__':
    # Original Kata: https://www.codewars.com/kata/585d7d5adb20cf33cb000235/

    read_values = [
        ['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a'],  # 'BbBb'
        ['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba'],  # 'foo'
        ['    ', 'a', '  '],  # 'a'
    ]

    for item in read_values:
        print(find_uniq(item))
