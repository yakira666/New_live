from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        elems = number.split("-")
        if len(elems) == 4:
            for i in elems:
                if len(i) == 4 and i.isdigit():
                    continue
                else:
                    return False
            return True
        return False

    @classmethod
    def check_name(cls, name):
        elems = name.split()
        if len(elems) == 2:
            for i in elems:
                for j in i:
                    if j not in cls.CHARS_FOR_NAME:
                        return False
                    continue
            return True

        return False
