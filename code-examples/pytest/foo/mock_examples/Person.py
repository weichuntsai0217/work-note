from .func1 import fn1
from .others import fn2
from .Fruit import Fruit

class Person(object):
    def __init__(self, person_name, fruit_name):
        self.name = person_name
        self.fruit = Fruit(fruit_name)

    def get_person_name(self):
        return self.name

    def get_fruit_name(self):
        return self.fruit.get_name()

    def get_num1(self, x): return fn1(x)

    def get_num2(self, x): return fn2(x)

    def get_whatever(self):
        return '{}{}'.format('whatever', self.get_person_name())
