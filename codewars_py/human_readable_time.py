def make_readable(seconds):
    hh = seconds // 3600
    mm = (seconds % 3600) // 60
    ss = seconds % 60
    return f'{hh:0>2}:{mm:0>2}:{ss:0>2}'


if __name__ == '__main__':
    # Original kata: https://www.codewars.com/kata/52685f7382004e774f0001f7/train
    test = [
        0,
        5,
        60,
        86399,
        359999,

    ]

    for i in test:
        print(make_readable(i))
