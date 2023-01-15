def find_the_number_plate(customer_id):
    return "".join([chr(97 + (customer_id // 999) % 26), chr(97 + (customer_id // 25974) % 26),
                    chr(97 + (customer_id // 675324) % 26), str(customer_id % 999 + 1).zfill(3)])


if __name__ == "__main__":

    # aaa004, baa489, oba041, zzz999, aja802, rba100, 
    read_packages = [3, 1487, 40000, 17558423, 234567, 43056]

    for n in read_packages:
        print(find_the_number_plate(n))
