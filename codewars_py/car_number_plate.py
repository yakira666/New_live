def find_the_number_plate(customer_id):
    # return "".join([chr(97 + (customer_id // 999) % 26), chr(97 + (customer_id // 999 * 26) % 26),
    # chr(97 + (customer_id // (26 ** 2 * 999)) % 26), str(customer_id % 999 + 1).zfill(3)])
    return "{0}{1}{2}{3:0>3}".format(chr(97 + (customer_id // 999) % 26), chr(97 + (customer_id // (999 * 26)) % 26),
                                     chr(97 + (customer_id // (26 ** 2 * 999)) % 26), customer_id % 999 + 1)


# def find_the_number_plate(customer_id):
#     number = (customer_id % 999) + 1
#     serial = customer_id // 999

    # return f'{chr(97 + serial % 26)}{chr(97 + (serial // 26) % 26)}{chr(97 + (serial // (26 ** 2)) % 26)}{number:0>3}'


if __name__ == "__main__":

    # Original Kata: https://www.codewars.com/kata/5f25f475420f1b002412bb1f
    
    # aaa004, baa489, oba041, zzz999, aja802, rba100,
    read_packages = [3, 1487, 40000, 17558423, 234567, 43056]

    for n in read_packages:
        print(find_the_number_plate(n))
