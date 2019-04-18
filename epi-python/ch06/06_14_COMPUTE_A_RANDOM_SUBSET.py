from __future__ import print_function

def get_random_subset(n, k):
  """
    Note that the 6.14 solution provided by EPI is just try to keep space complexity (including output) is O(k)
    and not O(n) because k is less than n.
    If you use solution 6.11, the time complexity is still the same level as 6.14 solution.
    The time complexity is O(k).
    The space complexity (including output) is O(k).
  """
  import random
  table = {}
  for i in xrange(k):
    idx = random.randint(i, n - 1)
    data_1 = table[idx] if idx in table else None
    data_2 = table[i] if i in table else None
    if data_1 == None and data_2 == None:
      table[i] = idx
      table[idx] = i
    elif data_1 != None and data_2 == None:
      table[i] = data_1
      table[idx] = i
    elif data_1 == None and data_2 != None:
      table[i] = idx
      table[idx] = data_2
    else:
      table[i] = data_1
      table[idx] = data_2

  res = []
  for j in xrange(k):
    res.append(table[j])
  return res

def get_input():
  return 10, 4

def main():
  n, k = get_input()
  print(get_random_subset(n, k))

if __name__ == '__main__':
  main()
