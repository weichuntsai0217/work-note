from __future__ import print_function

def partition_repeated(array):
  """
    The time complexity is O(n) where n is the array length.
    The additional space complexity is O(m) where m is the number of distinct ages.
  """
  age_to_count = {}
  for s in array:
    if s[1] not in age_to_count:
      age_to_count[s[1]] = 0
    age_to_count[s[1]] += 1

  age_to_offset = {}
  offset = 0
  for key in age_to_count:
    age_to_offset[key] = offset
    offset += age_to_count[key]

  while age_to_offset:
    itr = iter(age_to_offset)
    key = itr.next()
    from_idx = age_to_offset[key]
    s = array[from_idx]
    to_idx = age_to_offset[s[1]]
    array[from_idx], array[to_idx] = array[to_idx], array[from_idx]
    age_to_count[s[1]] -= 1
    if age_to_count[s[1]] > 0:
      age_to_offset[s[1]] += 1
    else:
      del age_to_offset[s[1]]

  
def get_input(case=0):
  array = [('Greg',14), ('John',12), ('Andy',11), ('Jim',13), ('Phil',12), ('Bob',13), ('Chip',13), ('Tim',14)]
  ans = [('Andy', 11), ('Phil', 12), ('John', 12), ('Chip', 13), ('Jim', 13), ('Bob', 13), ('Greg', 14), ('Tim', 14)]
  if case == 0:
    pass
  return array, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    array, ans = get_input(case)
    print('Input:')
    print('array =', array)
    partition_repeated(array)
    print('Output:')
    print('res =', array)
    print('ans =', ans)
    print('Test success' if array == ans else 'Test failure')

if __name__ == '__main__':
  main()




