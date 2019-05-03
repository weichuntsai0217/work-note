from __future__ import print_function

def eval_rpn(s): # we assume the input format is alway correct.
  """
    The time complexity is O(n) where n is the length of string.
    The additional space complexity is O(n).
  """
  symbols = s.split(',')
  stack = []
  for item in symbols:
    if item in '+-*/':
      y = stack.pop()
      x = stack.pop()
      if item == '+':
        stack.append(x + y)
      elif item == '-':
        stack.append(x - y)
      elif item == '*':
        stack.append(x * y)
      elif item == '/':
        stack.append(x / y)
    else:
      stack.append(int(item))
  return stack.pop()

def get_input(case=0):
  if case == 0:
    return '3,4,+,2,*,1,+', 15
  elif case == 1:
    return '-641,6,/,28,/', -4
  elif case == 2:
    return '3,4,+,2,5,6,*,*,*,1,+', 421
  elif case == 3:
    return '3,4,+,2,5,6,*,*,*,1,600,+,-', -181
  elif case == 4:
    return '3,4,+,2,5,6,*,*,*,1,100,+,/', 4

def main():
  for case in xrange(5):
    s, ans = get_input(case)
    res = eval_rpn(s)
    print('res =', res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
