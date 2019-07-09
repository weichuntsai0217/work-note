from __future__ import print_function
def get_power_set(array):
  """
    The time complexity is O(n * 2^n). 
    The additional space complexity (excluding res) is O(h) = O(n) where h is the tree height and is just the number of elements.
    The total space complexity (including res) is O(n * 2^n). 
    Take [0, 1, 2] as an example:
      The left child is not choosed, and the right child is choosed.
      So we have 2^3 = 8 path, each path defines a subset.
      Our solution just enumerate all paths.
      level
          0        0           0
          1     1     1     1     1
          2   2   2 2   2 2   2 2   2
  """
  def recursive(array, level, selected, res):
    if level == len(array):
      res.append([x for x in selected])
      return
    selected.append(array[level]) # choose this level and is equal to go to the right path.
    recursive(array, level+1, selected, res)
    selected.pop()  # Do not choose this level and is equal to go to the left path.
    recursive(array, level+1, selected, res)

  array.sort()
  res = []
  selected = []
  recursive(array, 0, selected, res)
  return res


def get_input(case=0):
  array = [0, 1, 2]
  ans = sorted([
    [],
    [0],
    [1],
    [2],
    [0, 1],
    [0, 2],
    [1, 2],
    [0, 1, 2],
  ])
  if case == 0:
    pass
  elif case == 1:
    array = [0, 1, 2, 3]
    ans = sorted([
      [],
      [0],
      [1],
      [2],
      [3],
      [0, 1],
      [0, 2],
      [0, 3],
      [1, 2],
      [1, 3],
      [2, 3],
      [1, 2, 3],
      [0, 2, 3],
      [0, 1, 3],
      [0, 1, 2],
      [0, 1, 2, 3],
    ])
  elif case == 2:
    array = [0, 1, 2, 3, 4]
    ans = sorted([
      [],
      [0],
      [1],
      [2],
      [3],
      [4],
      [0, 1],
      [0, 2],
      [0, 3],
      [0, 4],
      [1, 2],
      [1, 3],
      [1, 4],
      [2, 3],
      [2, 4],
      [3, 4],
      [0, 1, 2],
      [0, 1, 3],
      [0, 1, 4],
      [0, 2, 3],
      [0, 2, 4],
      [0, 3, 4],
      [1, 2, 3],
      [1, 2, 4],
      [1, 3, 4],
      [2, 3, 4],
      [1,2,3,4],
      [0,2,3,4],
      [0,1,3,4],
      [0,1,2,4],
      [0,1,2,3],
      [0, 1, 2, 3, 4],
    ])
    
  return array, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    print('Input:')
    array, ans = get_input(case)
    print('array =', array)
    print('Output:')
    res = sorted(get_power_set(array))
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

