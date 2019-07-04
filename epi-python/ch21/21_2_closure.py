"""
  Use python 3.6.8
"""
"""
  # What is a closure?
  A closure is the combination of a function and the lexical environment within which that function was declared.
  The references are below
  * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
  * https://en.wikipedia.org/wiki/Closure_(computer_programming)

  # What is a variable scope?
  A variable scope (or a scope) is a code area which determines the accessibility of variables.

  # What is a function scope?
  A function scope is a code area inside a function.

  # What is a class scope
  A class scope is a code area inside a class.

  # What is a global scope?
  A global scope is acutual the area within a module file but not within the function scopes and class scopes.

  # What is a local variable?
  A local variable is a variable declared in a function.

  # What is an enclosing variable (free variable)?
  An enclosing variable (free variable) is a variable declared in the area which encloses the declaration of the current function.
  For example,
  ```
  def outer():
    x = 1
    def inner():
      return x + 1
  ```
  then `x` defined in `outer` is an enclosing variable relative to the function `inner`.

  # How Python finds variables?
  It follows LEGB order, that is Local, Enclosing, Global(module), and Built-in.

  # How to check a closure which a function can see?
  Use the attribute `__closure__`
  Here is the reference
  * https://medium.com/@dboyliao/%E8%81%8A%E8%81%8A-python-closure-ebd63ff0146f

"""

def is_all_closure_equal(fns):
  for i in range(1, len(fns)):
    if fns[i].__closure__ != fns[i-1].__closure__:
      return False
  return True

print('===== Case 1 =====')
"""
  Note that in Python 3, the single line for loop in list or tuple construction
  would not add the dummy index into global.
"""
increment_by_i_case_1 = [lambda x: x + i for i in range(10)]
print('increment_by_i_case_1[3](4) =', increment_by_i_case_1[3](4))
print('is_all_closure_equal ?', is_all_closure_equal(increment_by_i_case_1))
print('That is why every fn increment_by_i_case_1 see the same latest i = 9')

print('===== Case 2 =====')
increment_by_i_case_2 = []
for i in range(10):
  increment_by_i_case_2.append(lambda x: x + i)
print('i =', i)
print('increment_by_i_case_2[3](4) =', increment_by_i_case_2[3](4))
print('is_all_closure_equal ?', is_all_closure_equal(increment_by_i_case_2))
print('That is why every fn increment_by_i_case_2 see the same latest i = 9')

print('===== Case 3 =====')
def gen_increment_by_i(i):
  # create a function scope to copy & store i to form a new closure.
  return lambda x: x + i
increment_by_i_case_3 = [gen_increment_by_i(i) for i in range(10)]
print('increment_by_i_case_3[3](4) =', increment_by_i_case_3[3](4))
print('is_all_closure_equal ?', is_all_closure_equal(increment_by_i_case_3))
print('That is why every fn in increment_by_i_case_3 see the different i.')

print('===== Case 4 =======')
def show_increment(start = 0):
  i = start
  def show():
    nonlocal i
    print(i)
    i += 1
  return show
show = show_increment(11)
for j in range(5):
  show()


print('===== Case 5 =======')
print('This case should not cause any error because of the closure.')
def foo():
    def bar():
        print('In bar')
        return bar # Error? This would not cause errors because of closure.
    return bar
bar = foo() # Error? This would not cause errors because of closure.
bar()

print('===== Case 6 ======')
print('If a function and its inner functions do not use enclosing variables, the __closure__ would be None')
def foo():
    a = 3
    def bar():
        print("bar")
    return bar
bar = foo()
print('bar.__closure__ is', bar.__closure__)

print('===== Case 7 ======')
print('If a function or its inner functions use enclosing variables, the __closure__ would Not be None')
def foo():
    a = 3
    b = 4
    def bar():
        def hell():
            return a, b
        return hell
    return bar
bar = foo()
hell = bar()
print('bar.__closure__ == hell.__closure__ ?', bar.__closure__ == hell.__closure__)
print('bar.__closure__ =', bar.__closure__)
print('bar.__closure__[0].cell_contents =', bar.__closure__[0].cell_contents)
print('bar.__closure__[1].cell_contents =', bar.__closure__[1].cell_contents)

print('===== Case 8 ======')
print('If a function or its inner functions use enclosing variables, the __closure__ would Not be None')
def foo():
    a = 3
    b = 4
    def bar():
        c = 5
        def hell():
            return a, b, c
        return hell
    return bar
bar = foo()
hell = bar()
print('bar.__closure__ == hell.__closure__ ?', bar.__closure__ == hell.__closure__)
print('bar.__closure__ =', bar.__closure__)
print('bar.__closure__[0].cell_contents =', bar.__closure__[0].cell_contents)
print('bar.__closure__[1].cell_contents =', bar.__closure__[1].cell_contents)
print('hell.__closure__ =', hell.__closure__)
print('hell.__closure__[0].cell_contents =', hell.__closure__[0].cell_contents)
print('hell.__closure__[1].cell_contents =', hell.__closure__[1].cell_contents)
print('hell.__closure__[2].cell_contents =', hell.__closure__[2].cell_contents)
