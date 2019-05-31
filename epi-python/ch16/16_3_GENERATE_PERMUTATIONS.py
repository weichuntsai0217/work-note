from __future__ import print_function

def get_all_permutations(array):
  def recursive(array, prefix, used, res):
    if len(array) == len(prefix):
      res.append([x for x in prefix])
      return
    for i in xrange(len(array)):
      if not used[i]:
        prefix.append(array[i])
        used[i] = True
        recursive(array, prefix, used, res)
        prefix.pop()
        used[i] = False
  res = []
  used = [False] * len(array)
  for i in xrange(len(array)):
    prefix = []
    if not used[i]:
      prefix.append(array[i])
      used[i] = True
      recursive(array, prefix, used, res)
      prefix.pop()
      used[i] = False
  return res

def get_all_permutations_epi_1(array):
  """
    The time complexity is O(n * n!)
    The additional space complexity is O(n!)
  """
  def direct_permutions(i, array, res):
    if i == len(array) - 1:
      res.append([x for x in array])
      return
    
    for j in xrange(i, len(array)):
      array[i], array[j] = array[j], array[i]
      direct_permutions(i + 1, array, res)
      array[i], array[j] = array[j], array[i]

  res = []
  direct_permutions(0, array, res)
  return res

def get_all_permutations_epi_2(array):
  """
    The time complexity is O(n * n!)
    The additional space complexity is O(1).
  """
  from ch16_utils import get_next_permutation
  array.sort()
  res = [[x for x in array]]
  while True:
    a = get_next_permutation(array)
    if a:
      res.append([x for x in a])
    else:
      return res


def get_input(case=0):
  array = [1,2,3]
  ans = sorted([
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
  ])
  if case == 0:
    pass
  elif case == 1:
    array = [1,2,3,4]
    ans = sorted([
      [1, 2, 3, 4],
      [1, 2, 4, 3],
      [1, 3, 2, 4],
      [1, 3, 4, 2],
      [1, 4, 2, 3],
      [1, 4, 3, 2],
      [2, 1, 3, 4],
      [2, 1, 4, 3],
      [2, 3, 1, 4],
      [2, 3, 4, 1],
      [2, 4, 1, 3],
      [2, 4, 3, 1],
      [3, 1, 2, 4],
      [3, 1, 4, 2],
      [3, 2, 1, 4],
      [3, 2, 4, 1],
      [3, 4, 1, 2],
      [3, 4, 2, 1],
      [4, 1, 2, 3],
      [4, 1, 3, 2],
      [4, 2, 1, 3],
      [4, 2, 3, 1],
      [4, 3, 1, 2],
      [4, 3, 2, 1],
    ])
    
  return array, ans

def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    print('Input:')
    array, ans = get_input(case)
    print('array =', array)
    print('Output:')
    res = sorted(get_all_permutations_epi_1(array))
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
