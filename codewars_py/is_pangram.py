def is_pangram(s):
    special_meanings = set(s.lower())
    asccii_char = 96
    while True:
        asccii_char += 1
        if chr(asccii_char) in special_meanings:
            continue
        else:
            break
    if asccii_char >= 122:
        return True
    else:
        return False


def is_pangram(s):
    s = s.upper()
    
    for i in range(65, 91):
        if chr(i) not in s:
            return False    

    return True


if __name__ == '__main__':
    
    # Original Kata: https://www.codewars.com/kata/545cedaa9943f7fe7b000048
    
    print(is_pangram("Aacdefghijklmnopqrstuvwxyz"))
    