from __future__ import print_function

def get_pascal(n):
  """
    Time complexity is O(n^2)
    Additional space complexity is O(n^2)
  """
  if n <= 0: return []
  res = [[1]]
  for i in xrange(1, n):
    res.append([])
    for j in xrange(i+1):
      if j == 0 or j == i:
        res[i].append(1)
      else:
        res[i].append(res[i-1][j] + res[i-1][j-1])

  return res

def get_input(case=0):
  if case == 0:
    n = 5
    ans = [
      [1],
      [1, 1],
      [1, 2, 1],
      [1, 3, 3, 1],
      [1, 4, 6, 4, 1],
    ]
  elif case ==1:
    n = 1
    ans = [[1]]
  elif case ==2:
    n = 0
    ans = []
  return n, ans


def main():
  for arg in xrange(3):
    n, ans = get_input(arg)
    res = get_pascal(n)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
