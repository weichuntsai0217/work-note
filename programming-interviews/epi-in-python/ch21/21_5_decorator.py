"""
  Use python 3.6.8
"""
"""
  # Question: Explain waht a decorator with an example that shows why it is useful.
  A decorator is a syntactic sugar to add new functionality in a function without modify its original functionality.
  and we can call the original function as usual.

  Just like its name, you can imagine that a decorator 'decorates' a function by another function.

  A very good reference for python decorators is https://foofish.net/python-decorator.html.

  By the way, after a funtion is decorated, the original __name__ and __doc__ would be changed by decorator.
  So, to fix this issue, you can use functools.wraps to keep the decorated function's __name__ and __doc__
  the same as its original.

  The decorator exmaple is as follows.
"""
import time
import timeit
import functools

def time_function(f, *args, **kwargs):
  """
    Print how long a function takes to compute.
  """
  begin = timeit.default_timer()
  result = f(*args, **kwargs)
  end = timeit.default_timer()
  delta = end - begin
  unit = 's'
  print('Function takes {} {} to execute'.format(delta, unit))
  return result

def foo_1(s):
  print('I am foo_1, and I would return {}'.format(s))
  return s

##########

def time_wrapper(f):
  def wrapper(*args, **kwargs):
    begin = timeit.default_timer()
    result = f(*args, **kwargs)
    end = timeit.default_timer()
    delta = end - begin
    unit = 's'
    print('Function takes {} {} to execute'.format(delta, unit))
    return result
  return wrapper

@time_wrapper # what the decorator did is just foo_2 = time_wrapper(foo_2)
def foo_2(s):
  """
    This is foo_2's doc.
  """
  print('I am foo_2, and I would return {}'.format(s))
  return s

##########

def time_wrapper_with_unit(unit='s'):
  def decorator(f):
    def wrapper(*args, **kwargs):
      begin = timeit.default_timer()
      result = f(*args, **kwargs)
      end = timeit.default_timer()
      delta = end - begin
      if unit == 'ms':
        delta *= 1000
      print('Function takes {} {} to execute'.format(delta, unit))
      return result
    return wrapper
  return decorator

@time_wrapper_with_unit('ms') # what the decorator did is just foo_3 = time_wrapper_with_unit('ms')(foo_2)
def foo_3(s):
  print('I am foo_3, and I would return {}'.format(s))
  return s

##########

def time_wrapper_with_wrapper_msg(f):
  def wrapper(*args, **kwargs):
    print('In wrapper: f.__name__ =', f.__name__)
    print('In wrapper: f.__doc__ =', f.__doc__)
    begin = timeit.default_timer()
    result = f(*args, **kwargs)
    end = timeit.default_timer()
    delta = end - begin
    unit = 's'
    print('Function takes {} {} to execute'.format(delta, unit))
    return result
  return wrapper

@time_wrapper_with_wrapper_msg
def foo_4(s):
  """
    This is foo_4's doc.
  """
  print('I am foo_4, and I would return {}'.format(s))
  return s

##########

"""
The implementation of functools.wraps is like below:
```
  def wraps(f):
    name = f.__name__
    doc = f.__doc__
    def decorator(func):
      func.__name__ = name
      func.__doc__ = doc
      return func
    return decorator
```
"""

def time_wrapper_keep_same_name_and_doc(f):
  @functools.wraps(f)
  def wrapper(*args, **kwargs):
    print('In wrapper: f.__name__ =', f.__name__)
    print('In wrapper: f.__doc__ =', f.__doc__)
    begin = timeit.default_timer()
    result = f(*args, **kwargs)
    end = timeit.default_timer()
    delta = end - begin
    unit = 's'
    print('Function takes {} {} to execute'.format(delta, unit))
    return result
  return wrapper

@time_wrapper_keep_same_name_and_doc
def foo_5(s):
  """
    This is foo_5's doc.
  """
  print('I am foo_5, and I would return {}'.format(s))
  return s

##########

def a(f):
  def wrapper(*args, **kwargs):
    print('Decorated by a')
    return f(*args, **kwargs)
  return wrapper

def b(f):
  def wrapper(*args, **kwargs):
    print('Decorated by b')
    return f(*args, **kwargs)
  return wrapper

def c(f):
  def wrapper(*args, **kwargs):
    print('Decorated by c')
    return f(*args, **kwargs)
  return wrapper

# The following 3 decorators would work on reverse order (cc -> bb -> aa),
# that is foo_6 = aa(bb(cc(foo_6)))
@a
@b
@c
def foo_6(s): # these 3 decorators would work on reverse order (c -> b -> a), that is foo_6 = a(b(c(foo_6)))
  print('I am foo_6, and I would return {}'.format(s))
  return s

##########

def title(s):
  print('\n=== ' + s + ' ===')

def show_res(res):
  print('The result is', res)

def main():
  title('Original call')
  res = foo_1('test_1')
  show_res(res)

  title('Without decorator, I want to trace the computing time of every foo_1 called in my program')
  res = time_function(foo_1, 'test_1')
  # This means every line which calls foo_1('test_1') should be rewritten as time_function(foo_1, 'test_1').
  # You have to take a lot of time to modify your code...
  show_res(res)

  title('Use decorator to trace the computing time of every foo_2 called in my program')
  res = foo_2('test_2') # Yeah! I just add a line before the declaration of foo_2 and everything is done.
  show_res(res)

  title('A decorator can accept parameters')
  res = foo_3('test_3')
  show_res(res)

  title('A decorator can modify __name__ and __doc__ of the original function')
  res = foo_4('test_4')
  show_res(res)
  print('foo_4.__name__ =', foo_4.__name__)
  print('foo_4.__doc__ =', foo_4.__doc__)

  title('Use functools.wraps to keep __name__ and __doc__ of the original function unchanged')
  res = foo_5('test_5')
  show_res(res)
  print('foo_5.__name__ =', foo_5.__name__)
  print('foo_5.__doc__ =', foo_5.__doc__)

  title('We can combo decorators')
  res = foo_6('test_6')
  show_res(res)

if __name__ == '__main__':
  main()
