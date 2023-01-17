def digital_root(n):
    s = sum([int(el) for el in str(n)])
    if len(str(s)) == 1:
        return s
    return digital_root(s)


if __name__ == '__main__':
    # Original kata: https://www.codewars.com/kata/541c8630095125aba6000c00/train

    test = [
        16,
        942,
        132189,
        493193,

    ]

    for i in test:
        print(digital_root(i))
