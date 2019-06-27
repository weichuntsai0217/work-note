from __future__ import print_function
def get_subset_with_size_k(n, k):
  """
  """
  def recursive(cur, n, k, selected, res):
    if (len(selected) == k):
      res.append([x for x in selected])
      return
    if cur >= (n+1):
      return
    selected.append(cur) # choose this level and is equal to go to the right path.
    recursive(cur+1, n, k, selected, res)
    selected.pop()  # Do not choose this level and is equal to go to the left path.
    recursive(cur+1, n, k, selected, res)

  res = []
  selected = []
  recursive(1, n, k, selected, res)
  return res


def get_input(case=0):
  n = 5
  k = 2
  ans = sorted([
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5],
    [2, 3],
    [2, 4],
    [2, 5],
    [3, 4],
    [3, 5],
    [4, 5],
  ])
  if case == 0:
    pass
    
  return n, k, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    print('Input:')
    n, k, ans = get_input(case)
    print('n =', n)
    print('k =', k)
    print('Output:')
    res = sorted(get_subset_with_size_k(n, k))
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

