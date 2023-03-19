# from home import House, SmallHouse


class Human:
    default_name = "Нет имени"
    default_age = 0

    def __init__(self, name: str = default_name, age: int = default_age) -> None:
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self) -> None:
        print(f'Имя: {self.name}\nВозраст: {self.age}\nДом: {self.__house}\nДенег: {self.__money}')

    @staticmethod
    def default_info() -> None:
        print(f'default name:{Human.default_name}\ndefault age: {Human.default_age}')

    def __make_deal(self, house, price) -> None:
        self.__money -= price
        self.__house = house

    def earn_money(self, amount: int) -> None:
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')

    def buy_house(self, house, discount) -> None:
        price = house.final_price(discount)
        if self.__money < price:
            print("Не достаточно денег")
        else:
            self.__make_deal(house, price)


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Окончательная цена: {final_price}')
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':

    Human.default_info()

    alexander = Human('Sasha', 27)
    alexander.info()

    small_house = SmallHouse(8_500)

    alexander.buy_house(small_house, 5)

    alexander.earn_money(5_000)
    alexander.buy_house(small_house, 5)

    alexander.earn_money(20_000)
    alexander.buy_house(small_house, 5)
    alexander.info()

"""
default name:Нет имени
default age: 0
Имя: Sasha
Возраст: 27
Дом: None
Денег: 0
Окончательная цена: 8075.0
Не достаточно денег
Earned 5000 money! Current value: 5000
Окончательная цена: 8075.0
Не достаточно денег
Earned 20000 money! Current value: 25000
Окончательная цена: 8075.0
Имя: Sasha
Возраст: 27
Дом: <__main__.SmallHouse object at 0x0000020B6D267CD0>
Денег: 16925.0
"""