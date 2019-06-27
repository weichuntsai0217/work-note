from __future__ import print_function

def is_parentheses_ok(s):
  """
    The time complexity is O(n) where n is the length of s.
    The additional space complexity is O(1).
  """
  stack = []
  mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
  }
  for c in s:
    if c in mapping:
      stack.append(c)
    else:
      if stack and mapping[stack[-1]] == c:
        stack.pop()
      else:
        return False
  return len(stack) == 0

def get_input(case):
  if case == 0:
    return '([]){()}', True
  elif case == 1:
    return '[()[]{()()}]', True
  elif case == 2:
    return '[()[]{({[]{}})()}]', True
  elif case == 3:
    return '{)', False
  elif case == 4:
    return '()[]{()()', False
  elif case == 5:
    return '()[]{(})()', False
  elif case == 6:
    return ')', False
  elif case == 7:
    return '{{}', False

def main():
  for case in xrange(8):
    print('--- case {} ---'.format(case))
    print('Input:')
    s, ans = get_input(case)
    print('s =', s)
    print('ans =', ans)
    res = is_parentheses_ok(s)
    print('Output')
    print('res =', res)
    print('Test success' if res == ans else 'Test failure')


if __name__ == '__main__':
  main()
