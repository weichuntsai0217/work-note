"""
  Use python 3.6.8
"""
"""
  # Question: How is the with statement used?
  The with statement is used to wrap the execution of a block with methods defined by a context manager.
  A context manage is an object which implements __enter__ and __exit__ methods.

  The with statement is usually used to manage access of resources, for example,
  acquiring and releasing locks, opening and closing files.

  A typical usage of with is below:
  ```
    with `SomeContextMgr`:
      `Do something`
  ```
  In the above example, in the with block but before `Do something`, SomeContextMgr.__enter__ would be executed,
  then `Do something` is executed, and finally SomeContextMgr.__exit__ is executed.
  Note even though `Do something` could contains `return` statement, the with statement guarantees that
  SomeContextMgr.__exit__ must be executed always.

"""

def f1(lock):
  print('In f1:')
  with lock:
    print('lock.locked() =', lock.locked())
    print('aa')
    return 'bb' # Even though we have a return in `with` block, the `__exit__` is still triggered to release the lock.
    print('cc')

def main():
  import threading
  print('In main:')
  lock = threading.Lock()
  print('lock.locked() =', lock.locked())
  res = f1(lock)
  print('In main:')
  print('res =', res)
  print('lock.locked() =', lock.locked()) # the lock is released successfully in f1

if __name__ == '__main__':
  main()
