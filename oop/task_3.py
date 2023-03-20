class VersionManager:
    def __init__(self, version: str = "0.0.1"):
        self.version = version
        version = version.strip(" \'\"").split(".")
        self.maj = int(version[0])
        self.min = int(version[1])
        self.path = int(version[2])
        print(self.maj, self.min, self.path)

    def major(self):
        self.maj += 1
        self.min = 0
        self.path = 0
        self.version = f'{self.maj}.{self.min}.{self.path}'
        return self.version

    def minor(self):
        self.min += 1
        self.path = 0
        self.version = f'{self.maj}.{self.min}.{self.path}'
        return self.version

    def path(self):
        self.path = 1
        self.version = f'{self.maj}.{self.min}.{self.path}'
        return self.version

    def release(self):
        self.version = f'{self.maj}.{self.min}.{self.path}'
        return self.version

    def rollback(self):
        return self.version


if __name__ == "__main__":
    print(VersionManager())

    # Original kata = https://www.codewars.com/kata/5bc7bb444be9774f100000c3/train/python

    # print(assert_equals(VersionManager().release()))
    # print(assert_equals(VersionManager("").release()))
    # print(assert_equals(VersionManager("1.2.3.4").release()))
    # print(assert_equals(VersionManager("1.2.3.d").release()))
    # print(assert_equals(VersionManager("1").release()))
    # print(assert_equals(VersionManager("1.1").release()))
    # print(assert_equals(VersionManager().major().release()))
    # print(assert_equals(VersionManager("1.2.3").major().release()))
    # print(assert_equals(VersionManager("1.2.3").major().major().release()))
    # print(assert_equals(VersionManager("10.11.12").major().major().release()))
    # print(assert_equals(VersionManager("1.2.3").release()))
    """
    В этом ката мы собираемся имитировать систему управления версиями программного обеспечения.
    
    Вы должны реализовать VersionManagerкласс.
    
    Он должен принимать необязательный параметр, представляющий начальную версию. Ввод будет в одном из следующих 
    форматов: "{MAJOR}", "{MAJOR}.{MINOR}", или "{MAJOR}.{MINOR}.{PATCH}". После этого могут быть указаны 
    дополнительные значения, PATCHно их следует игнорировать.
    "Error occured while parsing version!"Если эти 3 части не являются десятичными значениями, 
    должно быть выдано исключение с сообщением . 
    Если начальная версия не указана или представляет собой пустую строку, используйте "0.0.1"по умолчанию.
    
    Этот класс должен поддерживать следующие методы, все из которых должны иметь цепочку (кроме release):
    
    major()- увеличить MAJOR на 1, установить MINOR и PATCH до0
    minor()- увеличить MINOR на 1, установить PATCH на 0
    patch()- увеличить PATCH на 1
    rollback()- вернуть значения MAJOR, MINOR, и PATCH до предыдущего вызова major// или выдать исключение с сообщением,
    minor если нет версии для отката. 
    Должны быть возможны несколько вызовов и восстановление истории версийpatch"Cannot rollback!"rollback()
    release()- вернуть строку в формате"{MAJOR}.{MINOR}.{PATCH}"
    
    Да прибудет с вами бинарная сила!
    """
