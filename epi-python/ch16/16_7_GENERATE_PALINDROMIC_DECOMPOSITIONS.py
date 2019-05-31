from __future__ import print_function

def is_palindromic(string, start, last):
  i = start
  j = last
  while i < j:
    if string[i] != string[j]:
      return False
    i += 1
    j -= 1
  return True

def gen_palindromic_decompositions(string):
  """
    The time complexity is O(n * 2^n)
    The additional space complexity is O(n)
  """
  def recursive(string, start, sol, res):
    if start == len(string):
      res.append([x for x in sol])
      return
    for last in xrange(start, len(string)):
      if is_palindromic(string, start, last):
        sol.append(string[start:last+1])
        recursive(string, last+1, sol, res)
        sol.pop()

  res = []
  sol = []
  recursive(string, 0, sol, res)
  return res

def get_input(case=0):
  string = 'abba'
  ans = sorted([
    ['a', 'b', 'b', 'a'],
    ['a', 'bb', 'a'],
    ['abba'],
  ])
  if case == 0:
    pass
  elif case == 1:
    string = ''
    ans = [[]]
  elif case == 2:
    string = '0204451881'
    ans = [
      ['0', '2', '0', '4', '4', '5', '1', '8', '8', '1'],
      ['0', '2', '0', '4', '4', '5', '1', '88', '1'],
      ['0', '2', '0', '4', '4', '5', '1881'],
      ['0', '2', '0', '44', '5', '1', '8', '8', '1'],
      ['0', '2', '0', '44', '5', '1', '88', '1'],
      ['0', '2', '0', '44', '5', '1881'],
      ['020', '4', '4', '5', '1', '8', '8', '1'],
      ['020', '4', '4', '5', '1', '88', '1'],
      ['020', '4', '4', '5', '1881'],
      ['020', '44', '5', '1', '8', '8', '1'],
      ['020', '44', '5', '1', '88', '1'],
      ['020', '44', '5', '1881'],
    ]
  return string, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    print('Input:')
    string, ans = get_input(case)
    print('string =', string)
    print('Output:')
    res = sorted(gen_palindromic_decompositions(string))
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()



