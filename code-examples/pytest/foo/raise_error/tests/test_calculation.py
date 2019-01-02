import pytest
from foo.raise_error.calculation import divide

def test_divide_nonzero():
    assert divide(2, 1) == 2
    assert divide(2, 2) == 1

def test_divide_zero():
    with pytest.raises(TypeError):
        divide(2, 0)
