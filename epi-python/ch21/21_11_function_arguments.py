"""
  Use python 3.6.8
"""
"""
  # What are positional arguments?
  On calling side, positional arguments are arguments without names

  # What are keyword arguments?
  On calling side, keyword arguments are arguments with names. Also, keyword arguments must come after all
  positional arguments.

  # What are default arguments?
  On function declaration side, default arguments are arguments with default values. If the function
  is called without passing arguments, the arguments get default values.

  # What does the function `test` outputs and why?
  One thing with default arguments is that they are evaluated once when the module is loaded,
  and they are shared across all callers.
  That's why `test` shows '[1]' and '[1,1]'.
  Usually we don't use mutable objects for default values.
  It is highly recommended that we set default values as None
  and in the function block we set the arguments into the real default values we want if
  we detect that the arguments are None.



"""

def foo(x,y,z):
  return x * x + y * y + z * z

def test():
  def foo(x=[]):
    x.append(1)
    return x
  print(foo())
  print(foo())

def main():
  print(foo(1, 2, 3))
  print(foo(x=1, y=2, z=3))
  print(foo(1, y=2, z=3)) # 1 is a positional argument, y and z are keyword arguments
  print(foo(1, z=3, y=2))
  print(foo(z=3, y=2, x=1))
  # foo(x=1, 2, z=3) # Syntax error, keyword arguments must come after all positional arguments
  # foo(1, x=2, z=3, y=4) # Syntax error, the variable x cannot be assigned twice.
  test()

if __name__ == '__main__':
  main()
