from unittest import mock
import pytest
from foo.mock_examples.others import fn2, fn3, get_fruit_info

"""
Case 1: mock fn1 in fn2
A super important thing you should know is that
even though fn1 is defined in module foo.mock_examples.func1,
the mock path is actually 'foo.mock_examples.others.fn1'
because it means 'fn1 imported in foo.mock_examples.others'
"""
@mock.patch('foo.mock_examples.others.fn1')
def test_fn2(mock_fn1):
    mock_fn1.return_value = 3
    res = fn2(4) # 3 + 5*4
    assert mock_fn1.call_count == 1
    mock_fn1.assert_called_with(4)
    assert res == 23

"""
Case 2: mock fn1 & fn2 in fn3
Be careful about the args order, it is the reverse of the mock.patch order.
"""
@mock.patch('foo.mock_examples.others.fn1')
@mock.patch('foo.mock_examples.others.fn2')
def test_fn3(mock_fn2, mock_fn1):
    mock_fn1.return_value = 4
    mock_fn2.return_value = 7
    res = fn3(8) # 4 + 2*7 + 3*8 = 42
    assert mock_fn1.call_count == 1
    assert mock_fn2.call_count == 1
    mock_fn1.assert_called_with(8)
    mock_fn2.assert_called_with(8)
    assert res == 42

"""
Case 3: mock.patch would not affect other tests.
We have mocked fn1 in fn3 in test_fn3.
However the mock in test_fn3 would not mock fn1 in 
the following test_fn3_with_only_mock_fn2 example.
"""
@mock.patch('foo.mock_examples.others.fn2')
def test_fn3_with_only_mock_fn2(mock_fn2):
    mock_fn2.return_value = 7
    res = fn3(8)
    # 8**2 + 2*7 + 3*8 = 102
    assert mock_fn2.call_count == 1
    mock_fn2.assert_called_with(8)
    assert res == 102

"""
Case 4: mock the class Fruit in get_fruit_info
"""
@mock.patch('foo.mock_examples.others.Fruit')
def test_get_fruit_info(mock_Fruit):
    instance = mock_Fruit.return_value
    instance.get_name.return_value = 'My mock name is apple.'
    res = get_fruit_info('banana')
    mock_Fruit.assert_called_with('banana')
    assert instance.get_name.called
    assert instance.get_name.call_count == 1
    assert res == 'My mock name is apple.'

"""
Case 5: mock fn1 & fn2 in fn3 with parametrize arg
Be careful about the args order, it is the reverse of the mock.patch order.
"""
@pytest.mark.parametrize('arg, expected', [
    (20, 78), # arg = 20, expected = 78
    (18, 72), # arg = 18, expected = 72
    (16, 66)  # arg = 16, expected = 66
])
@mock.patch('foo.mock_examples.others.fn1')
@mock.patch('foo.mock_examples.others.fn2')
def test_fn3(mock_fn2, mock_fn1, arg, expected):
    mock_fn1.return_value = 4
    mock_fn2.return_value = 7
    res = fn3(arg) # 4 + 2*7 + 3*arg = expected
    assert mock_fn1.call_count == 1
    assert mock_fn2.call_count == 1
    mock_fn1.assert_called_with(arg)
    mock_fn2.assert_called_with(arg)
    assert res == expected
