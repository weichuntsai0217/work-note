from .func1 import fn1
from .Fruit import Fruit

def fn2(x):
    return fn1(x) + 5*x

def fn3(x):
    return fn1(x) + 2*fn2(x) + 3*x

def get_fruit_info(fruit_name):
    fruit = Fruit(fruit_name)
    return fruit.get_name()
