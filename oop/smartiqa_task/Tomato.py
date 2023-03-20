# class Tomato:
#     states = {0: "Отсутствует", 1: "Цветение", 2: "Зеленый", 3: "Красный"}
#
#     def __init__(self, _index):
#         self._index = _index
#         self._state = 0
#
#     def grow(self):
#         self._change_state()
#
#     def is_ripe(self):
#         if self._state == 3:
#             return True
#         return False
#
#     def _change_state(self):
#         if self._state < 3:
#             self._state += 1
#         else:
#             print(f'Tomato {self._index} сейчас {Tomato.states[self._state]}')
#
#
# class TomatoBush:
#
#     def __init__(self, quantity):
#         self.tomatoes = [Tomato(i) for i in range(quantity)]
#         print(self.tomatoes)
#
#     def grow_all(self):
#         for i in self.tomatoes:
#             i.grow()
#
#     def all_are_ripe(self):
#         for i in self.tomatoes:
#             return i.is_ripe()
#
#     def give_away_all(self):
#         self.tomatoes = []
#
#
# class Gardener:
#
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     def work(self):
#         print("Working...")
#         self._plant.grow_all()
#
#     def harvest(self):
#         if
#
#
# TomatoBush.grow_all()
# TomatoBush.grow_all()
# TomatoBush.grow_all()
# print(TomatoBush(5).all_are_ripe())

