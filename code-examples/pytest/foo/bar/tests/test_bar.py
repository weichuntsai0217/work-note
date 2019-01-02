import pytest
from foo.bar.bar1 import b1
from foo.bar.bar2 import b2

argstr = 'arg, expected'

data = [
    (20, 19),
    (18, 17),
    (16, 15)
]

def test_b1():
    assert b1(2) == 30

def test_b2():
    assert b2(16) == 15

@pytest.mark.parametrize('arg, expected', [
    (20, 19),
    (18, 17),
    (16, 15)
])
def test_b2_multiple_inputs_by_parametrize_1(arg, expected):
    assert b2(arg) == expected

@pytest.mark.parametrize(argstr, data)
def test_b2_multiple_inputs_by_parametrize_2(arg, expected):
    assert b2(arg) == expected
