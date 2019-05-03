from __future__ import print_function

def normalize_path(path):
  """
    The time complexity is O(n) where n is the length of the string (path)
    The additional space complexity is O(n) => from the split part
  """
  items = filter(lambda x: (x != '' and x != '.'), path.split('/'))
  stack = []
  for item in items:
    if stack and (stack[-1] != '..') and (item == '..'):
      stack.pop()
    else:
      stack.append(item)
  if not stack:
    return '/' if path[0] == '/' else './'
  res = '/' + '/'.join(stack) if path[0] == '/' else '/'.join(stack)
  if stack[-1] == '..':
    res += '/'
  return res

def get_input(case):
  if case == 0:
    path = '/usr/lib/../bin/gcc'
    ans = '/usr/bin/gcc'
    return path, ans
  elif case == 1:
    path = 'scripts//./../scripts/awkscripts/././'
    ans = 'scripts/awkscripts'
    return path, ans
  elif case == 2:
    path = 'aaa/.//bbb//.//./../../'
    ans = './'
    return path, ans
  elif case == 3:
    path = '/aaa/.//bbb//.//./../../'
    ans = '/'
    return path, ans
  elif case == 4:
    path = './'
    ans = './'
    return path, ans
  elif case == 5:
    path = '../'
    ans = '../'
    return path, ans
  elif case == 6:
    path = '../../'
    ans = '../../'
    return path, ans
  elif case == 7:
    path = '../aa'
    ans = '../aa'
    return path, ans
def main():
  for case in xrange(8):
    print('--- case {} ---'.format(case))
    print('Input:')
    path, ans = get_input(case)
    print('path =', path)
    print('ans =', ans)
    res = normalize_path(path)
    print('Output')
    print('res =', res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
