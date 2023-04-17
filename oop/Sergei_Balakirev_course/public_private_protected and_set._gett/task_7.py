from string import ascii_lowercase, digits
import random


class EmailValidator:
    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        """Генерация случайного Е-майла"""
        l_mail = "".join(random.choice(ascii_lowercase + ascii_lowercase.upper() + digits + "_" + ".") for _ in
                         range(random.randint(1, 100)))
        r_mail = "".join(random.choice(ascii_lowercase + ascii_lowercase.upper() + digits + "_") for _ in
                         range(random.randint(2, 50)))
        full_eml = l_mail + "@" + r_mail.replace(random.choice(r_mail[:len(r_mail)]), ".", 1)
        return full_eml

    @classmethod
    def check_email(cls, email):
        a = "".join(ascii_lowercase + ascii_lowercase.upper() + digits + "_" + "." + "@")
        try:
            if (EmailValidator.__is_email_str(email)) and (set(email).issubset(set(a)) and (len(email.split("@")[0]) <= 100) and (
                    len(email.split("@")[1]) <= 50)) and ("." in (email[email.find("@")::])) and (
                    ".." not in email):
                return True
        except:
            return False
        return False

    @staticmethod
    def __is_email_str(email):
        if isinstance(email, str):
            return True
        return False


if __name__ == "__main__":
    assert EmailValidator.check_email(EmailValidator.get_random_email()) == True
    assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
    assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
    assert EmailValidator.check_email('name.surname@mail.com') == True
    assert EmailValidator.check_email(1342) == False
    assert EmailValidator.check_email('a+a@m.c') == False
    assert EmailValidator.check_email('aabda..kkk@m.c') == False
    assert EmailValidator.check_email('aaaa@bbb..cc') == False
    assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
    assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
    assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
    assert EmailValidator.check_email('name.surnamemail.com') == False
    assert EmailValidator.check_email('name@mail') == False
