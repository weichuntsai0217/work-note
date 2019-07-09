"""
  Use python 3.6.8
"""
"""
  # Question: Explain the rules for variable scope
  
  There are two possibilities: the variable apears in an expression, and the variable is being assigned to.
  
  ## When the variable apears in an expression, Python searches for it in the following order.
  1. The current function
  2. Enclosing scope, e.g., containing functions.
  3. The module containing the code (also referred to as the global scope)
  4. The built-in scope, e.g., open.
  A NameError is raised if none of these scopes contain a defined variable with the given name.

  ## When variable is being assigned to.
  1. To assign a local variable x to value 2 in the current function. Don't use the keywords 'global' and 'nonlocal' and
     just write 'x = 2'. If this is the first time 'x = 2' happens in the current function, python would
     create a new local variable x in the current function.
  2. To assign a global variable x to value 2 in the current function. Use the keyword 'global' and write as follows:
     ```
     global x
     x = 2
     ```
  3. To assign a variable x in nested functions(enclosing functions) to value 2 in the current function.
     Use the keyword 'nonlocal' (only available in python 3) and write as follows:
     ```
     nonlocal x
     x = 2
     ```

"""

x, y, z = 'global-x', 'global-y', 'global-z'

def basic_scoping():
  print(x) # global-x
  y = 'local-y'
  global z
  z = 'local-z'

basic_scoping()
print(x, y, z) # global-x, global-y, local-z


def inner_outer_scoping():
  def inner1():
    print(x) # outer-x

  def inner2():
    x = 'inner2-x'
    print(x) # inner2-x

  def inner3():
    nonlocal x
    x = 'inner3-x'
    print(x) # inner3-x

  x = 'outer-x'
  inner1()
  inner2()
  inner3()
  print(x) # inner3-x

inner_outer_scoping()
print(x, y, z) # global-x, global-y, local-z


def outer_scope_error():
  def inner():
    try:
      x = x + 321
    except NameError:
      print('Error: x is local, and so x + 1 is not defined yet.')
  x = 123
  inner()

outer_scope_error() # Error: x is local, and so x + 1 is not defined yet.


def outer_scope_array_no_error():
  def inner():
    x[0] = -x[0] # x[0] isn't a variable, it's resolved from outer x.
  x = [314]
  inner()
  print(x[0]) # -314

outer_scope_array_no_error()


def outer_scope_error2():
  try:
    print(w)
  except NameError:
    print('Error: w is not defined yet even in global.') # Error: w is not defined yet even in global.

outer_scope_error2() # When Python goes to the global scope and try to find w, because the line `w = 'global-w'` is not executed, the global w is not defined.
w = 'global-w'

def outer_scope_success():
  print(v)
v = 'global-v'
outer_scope_success()
