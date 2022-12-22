def rgb(r, g, b):
    args = [r, g, b]
    word = ""
    for i in args:
        if int(i) > 255:
            word += f"{255:02x}".upper()
        elif int(i) < 0:
            word += f"{0:02x}".upper()
        else:
            word += f"{i:02x}".upper()
    return word


nums_conversions = list(int(i) for i in input().replace(",", "").strip("() ").split())
print(rgb(nums_conversions[0], nums_conversions[1], nums_conversions[2]))

