def ips_between(start, end):
    start_ip_array = start.split('.')
    end_ip_array = end.split('.')

    first_part = int(end_ip_array[3]) - int(start_ip_array[3])
    second_part = (int(end_ip_array[2]) - int(start_ip_array[2])) * 256
    third_part = (int(end_ip_array[1]) - int(start_ip_array[1])) * pow(256, 2)
    end_part = (int(end_ip_array[0]) - int(start_ip_array[0])) * pow(256, 3)

    return sum([first_part, second_part, third_part, end_part])

# print(ips_between("10.0.0.0", "10.0.0.50")) # => return 50
# print(ips_between("10.0.0.0", "10.0.1.0"))  # => return  256
# print(ips_between("20.0.0.10", "20.0.1.0")) # => return  246
# print(ips_between("89.172.177.44", "113.179.232.73"))

# 73.170.162.247 and 74.5.1.31, Expecting: 5922344
