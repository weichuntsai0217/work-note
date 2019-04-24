from __future__ import print_function

def get_n_th_look_and_say(n):
  """
    The time complexity is O(n * 2^n)
  """
  if n < 1: return None
  if n == 1: return '1'
  res = '1'
  for i in xrange(2, n+1):
    start = 0
    end = start + 1
    tmp = ''
    while start < len(res):
      if end < len(res) and res[end] == res[start]:
        end += 1
      else:
        tmp += (str(end - start) + res[start])
        start = end
    res = tmp
  return res
    
def get_input(case=1):
  if case == 1:
    return 1, '1'
  elif case == 2:
    return  2, '11'
  elif case == 3:
    return 3, '21'
  elif case == 4:
    return 4, '1211'
  elif case == 5:
    return 5, '111221'
  elif case == 6:
    return 6, '312211'
  elif case == 7:
    return 7, '13112221'
  elif case == 8:
    return 8, '1113213211'

def main():
  for case in xrange(1, 9):
    n, ans = get_input(case)
    res = get_n_th_look_and_say(n)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
