from __future__ import print_function

def increment_int(x):
  """
    Time complexity is O(n) where n is the length of x.
  """
  ca = 0
  last_idx = len(x) - 1
  for i in xrange(last_idx, -1, -1):
    if i == last_idx:
      if (x[i] + 1) >= 10:
        x[i] = 0
        ca = 1
      else:
        x[i] += 1
        break
    else:
      if (x[i] + ca) >= 10:
        x[i] = 0
        if i == 0:
          x.insert(0, 1)
      else:
        x[i] += ca
        break
  return x

def get_input(case=0):
  if case == 0:
    return [1,2,3], [1,2,4]
  elif case == 1:
    return [1,2,9], [1,3,0]
  elif case == 2:
    return [1,9,9], [2,0,0]
  elif case == 3:
    return [9,9,9], [1,0,0,0]

def main():
  for arg in xrange(4):
    x, ans = get_input(arg)
    res = increment_int(x)
    print(x)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
