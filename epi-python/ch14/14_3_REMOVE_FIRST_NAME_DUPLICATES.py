from __future__ import print_function

def remove_first_name_duplicates(array):
  """
    If you care about the order of the last name, then this solution is the best solution
    and can guarantee there is only one acceptable answer for one input array.
    The time complexity for this solution is O(n * logn) where n is the array length.
    The additional space complexity is O(1).

    If you don't care about the order of the last name, then you can consider to use a hash table
    to imporve the time complexity to O(n) (but with a trade-off that you have space complexity O(n)) and
    there could be multiple acceptable answers for one input array.
  """
  if len(array) <= 1: return array
  array.sort()
  res = [array[0]]
  i = 0
  j = 1
  while j < len(array):
    if array[i][0] != array[j][0]:
      res.append(array[j])
      i = j
    j += 1
  return res

  
def get_input(case=0):
  array = [('Ian', 'Botham'),('David', 'Gower'),('Ian', 'Bell'),('Ian', 'Chappell')]
  ans = [('David', 'Gower'), ('Ian', 'Bell')]
  if case == 0:
    pass
  elif case == 1:
    array.insert(0, ('Zoey', 'Bryant'))
    array.append(('Zoey', 'Bryan'))
    ans.append(('Zoey', 'Bryan'))
  return array, ans

def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    res = remove_first_name_duplicates(array)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()



