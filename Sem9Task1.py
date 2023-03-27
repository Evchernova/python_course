"""Реализовать дескрипторы для любых двух классов"""

class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Road:
    _length = NonNegative()
    _width = NonNegative()
    def __init__(self, _length=150, _width=200):
        self._length = _length
        self._width = _width
        print("Длина {} м, ширина {} м".format(self._length, self._width))

    def square(self):
        self.square_rd = self._length * self._width
        return self.square_rd


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


rd1 = Road(_length=150, _width=200)
r = MassCount(20, 5000, 25)
print(r.square())
