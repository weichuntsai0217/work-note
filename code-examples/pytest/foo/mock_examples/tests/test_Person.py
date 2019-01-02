from unittest import mock
from foo.mock_examples.Person import Person

"""
Case 1: test constructor of Person by mocking Fruit
"""
@mock.patch('foo.mock_examples.Person.Fruit')
def test_init(mock_Fruit):
    fruit = mock_Fruit.return_value
    obj = Person('John', 'banana')
    mock_Fruit.assert_called_with('banana')
    assert obj.name == 'John'
    assert obj.fruit == fruit

"""
Case 2: test get_person_name of Person
"""
def test_get_person_name():
    obj = Person('John', 'banana')
    assert obj.get_person_name() == 'John'

"""
Case 3: test get_fruit_name of Person by mocking get_name of Fruit
"""
@mock.patch('foo.mock_examples.Person.Fruit')
def test_get_fruit_name(mock_Fruit):
    fruit = mock_Fruit.return_value
    fruit.get_name.return_value = 'I am apple.'
    obj = Person('John', 'banana')
    assert obj.get_fruit_name() == 'I am apple.'
    assert fruit.get_name.called

"""
Case 4: test get_whatever of Person by mocking get_person_name of Person
"""
def test_get_whatever():
    obj = Person('John', 'banana')
    obj.get_person_name = mock.MagicMock(return_value='Mary')
    """
    the above line is equivalent to
    ```
    obj.get_person_name = mock.MagicMock()
    obj.get_person_name.return_value = 'Mary'
    ```
    """
    res = obj.get_whatever()
    assert res == '{}{}'.format('whatever', 'Mary')
    assert obj.get_person_name.called
    assert obj.get_person_name.call_count == 1
