
def find_min_max(x):
  """
    The time complexity is O(n)
  """
  if not x: return None
  if len(x) == 1:
    return x[0], x[0] # the first is min and the second is max
  min_val = x[0]
  max_val = x[0]
  for i in xrange(1, len(x)):
    if x[i] < min_val:
      min_val = x[i]
    elif x[i] > max_val:
      max_val = x[i]

def min_max(a, b):
  if a < b:
    return a, b
  return b, a

def find_min_max_fast(x):
  """
    The time complexity is O(n)
    Note that even though find_min_max_fast and find_min_max have the same order of time complexity,
    If you count the comparison operations carefully, you would find that
    find_min_max_fast takes O(3n/2 - 2) comparisons and
    find_min_max takes O(2n - 2) comparisons
  """
  import math
  if not x: return None
  if len(x) == 1:
    return x[0], x[0] # the first is min and the second is max
  min_val, max_val = min_max(x[0], x[1])
  for i in xrange(2, (len(x) - 1), 2):
    smaller, larger = min_max(x[i], x[i+1])
    min_val = min(smaller, min_val)
    max_val = max(larger, max_val)
  if len(x) & 1:
    # the length of x is odd.
    min_val = min(x[-1], min_val)
    max_val = max(x[-1], max_val)
  return min_val, max_val

def get_input(case=0):
  x = [3,2,5,1,2,4]
  ans_min = 1
  ans_max = 5
  if case == 0:
    pass
  return x, ans_min, ans_max
 
if __name__ == '__main__':
  for case in xrange(1):
    x, ans_min, ans_max = get_input(case)
    res_min, res_max = find_min_max_fast(x)
    print(res_min == ans_min)
    print(res_max == res_max)
  
