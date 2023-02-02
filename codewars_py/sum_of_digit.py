# def digital_root(n):
#     s = sum([int(el) for el in str(n)])
#     if len(str(s)) == 1:
#         return s
#     return digital_root(s)

def digital_root(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    if total < 10:  # Recursion exit condition
        return total

    return digital_root(total)  # recursive call


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
