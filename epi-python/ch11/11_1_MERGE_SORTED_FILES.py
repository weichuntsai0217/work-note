from __future__ import print_function
import heapq

def merge_lists(ls):
  """
    The time complexity is O(n*logk) where n is the total number of elements in input sequences and k is the number of
      sequences.
    The additional space complexity is O(k).
  """
  its = [iter(x) for x in ls]
  min_heap = []
  res = []
  
  for seq_id in xrange(len(its)):
    try:
      x = its[seq_id].next()
      heapq.heappush(min_heap, (x, seq_id)) # if you pass a tuple, heapq uses the tuple[0] as priority.
    except:
      pass
  
  while min_heap: # n times
    (val, seq_id) = heapq.heappop(min_heap) # logk
    res.append(val)
    try:
      x = its[seq_id].next()
      heapq.heappush(min_heap, (x, seq_id)) # logk
    except:
      pass

  return res

def merge_lists_brute_force(ls):
  """
    The time complexity is O(n*logn) where n is the number of total elements in ls
    The additional space complexity is O(1) (excluding the output)
  """
  res = []
  for l in ls:
    res += l
  return sorted(res)

def get_input(case=0):
  ls = None
  ans = None
  if case == 0:
    ls = [
      [3,5,7],
      [0,6],
      [0,6,28],
    ]
    ans = [0, 0, 3, 5, 6, 6, 7, 28]
  elif case == 1:
    ls = [
      [3,5,7],
      [],
      [0,6,28],
    ]
    ans = [0, 3, 5, 6, 7, 28]
  elif case == 2:
    ls = [
      sorted([4,2,5,7,9]),
      sorted([5,3,6,78,34]),
      sorted([0, 78]),
    ]
    ans = [0, 2, 3, 4, 5, 5, 6, 7, 9, 34, 78, 78]
  return ls, ans


def main():
  print('Use merge_lists_brute_force')
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    ls, ans = get_input(case)
    print('Input:')
    print('ls =', ls)
    res = merge_lists_brute_force(ls)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

  print('\n===============\n')
  print('Use merge_lists')
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    ls, ans = get_input(case)
    print('Input:')
    print('ls =', ls)
    res = merge_lists(ls)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
