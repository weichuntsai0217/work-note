"""
  Use python 3.6.8
"""
"""
  # Question: What are "*args" and "**kwargs" and Where are they appropriate?

  # A short answer: Both are used to pass a series of arguments to a function.
  We explain details in 2 scenarios below.

  ## Scenario 1: When use on function declaration
  `*args` is used to pass a series of positional arguments in order.
  * 'args' is just a name. You can use any name you want.
  * '*' is important and must be specified.
  * the '*' arguments must appear after all the regular arguments.
  * In function scope, the series of positional arguments you passed in would be wrapped into a tuple and
    assign to `args` (assume you declare as `*args`)

  `**kwargs` is used to pass a series of keyword arguments.
  * 'kwargs' is just a name. You can use any name you want.
  * '**' is important and must be specified.
  * the '**' arguments must appear after all the regular arguments and the '*' argument.
  * In function scope, the series of keyword arguments you passed in would be wrapped into a dict and
    assign to `kwargs` (assume you declare as `**kwargs`)

  ## Scenario 2: When use on calling a function
  If `args` is a tuple or a list, then `*args` would take each element out from `args` in order and feed the element
  into the function in order.
  If `kwargs` is a dict, then `**kwargs` would take each element out from `kwargs` by key and feed the element
  into the function by key.
"""

def foo(u, v, *args, **kwargs):
  print('u =', u)
  print('v =', v)
  print('args =', args)
  print('kwargs =', kwargs)

def bar(u, v, x, y, name=None, rank=None):
  print('u =', u)
  print('v =', v)
  print('x =', x)
  print('y =', y)
  print('name =', name)
  print('rank =', rank)

def main():
  
  print('=== The 1st way to feed arguments ===')
  foo(1, 'euler', 2.71, [6, 28], name='cfg', rank=1)

  print('\n')
  print('=== The 2nd way to feed arguments, it is the same as the 1st way ===')
  args = (2.71, [6, 28]) # use list is also OK, like:  [2.71, [6, 28]]
  kwargs = {
    'name': 'cfg',
    'rank': 1,
  }
  foo(1, 'euler', *args, **kwargs)

  print('\n')
  print('=== Another case ===')
  bar(1, 'euler', *args, **kwargs)

if __name__ == '__main__':
  main()
