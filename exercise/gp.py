# import random


# def randpasswd(length, chars=None):
#     if chars is None:
#         # if chars == None:  # ошибка
#         chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_+/*\\|<>;:"

#     return ''.join(random.choices(chars, k=length))


# if __name__ == '__main__':
#     print(randpasswd(64))

# ---------------------------------------

def get_password(length, special=None):
    from string import digits, ascii_letters
    from random import choices

    punctuation = '%*)(?@#$'
    all_symbols = digits + ascii_letters

    if special is not None:
        all_symbols += punctuation

    return ''.join(choices(all_symbols, k=length))


if __name__ == '__main__':
    from colorama import init, Fore, Style
    import sys
    import os

    init()

    try:
        length: int = int(sys.argv[1])

    except (ValueError, TypeError):
        print(f'{Fore.LIGHTYELLOW_EX}Entered non-numeric value...{Style.RESET_ALL}')
        print(f'{Fore.CYAN}Enter the correct value e.g. {Fore.GREEN}python3 {os.path.basename(__file__)} 12 -p{Style.RESET_ALL}')

    else:
        punc = None
        if '-p' in sys.argv[1:]:
            punc = True

        if not 8 <= length <= 32:
            print(f'{Fore.LIGHTBLUE_EX}The recommended minimum password length is 8 characters, maximum is 32 characters{Style.RESET_ALL}')

        if length > 0:
            print(
                f'Your password: {Fore.GREEN}{get_password(length, special=punc)}{Style.RESET_ALL}')
        else:
            print(f'{Fore.RED}Incorrect value...{Style.RESET_ALL}')
