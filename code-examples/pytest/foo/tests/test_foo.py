from foo.foo1 import f1
from foo.foo2 import f2

def test_f1():
    assert f1(2) == 3

def test_f2():
    assert f2(5) == 6
