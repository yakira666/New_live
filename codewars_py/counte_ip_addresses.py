def ips_between(start, end):
    """_summary_

    Args:
        start (_type_): _description_
        end (_type_): _description_

    Returns:
        _type_: _description_
    """
    start_ip_array = list(map(int, start.split('.')))
    end_ip_array = list(map(int, end.split('.')))

    count = 0
    for i in range(len(start_ip_array)):
        count += (end_ip_array[i] - start_ip_array[i]) * pow(256, 3 - i)

    return count


if __name__ == '__main__':

    read_package = [
        ("10.0.0.0", "10.0.0.50"),  # 50
        ("10.0.0.0", "10.0.1.0"),  # 256
        ("20.0.0.10", "20.0.1.0"),  # 246
        ("89.172.177.44", "113.179.232.73"),  # 403126045
    ]

    for item in read_package:
        print(ips_between(*item))
