"""Реализовать дескрипторы для любых двух классов"""


"""class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

a = Position('Михаил', 'Иванов', 'Инженер', 55000, 10000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
"""

class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Не может быть отрицательным.')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name
class Order:
    price = NonNegative()
    quantity = NonNegative()
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity
    def total(self):
        return self.price * self.quantity
carrot_order = Order('Морковь', 1, 10)
print(carrot_order.total())

carrot_order.price = 15
carrot_order.quantity = 10
print(carrot_order.total())

carrot_order.price = -15
carrot_order.quantity = 10
print(carrot_order.total())