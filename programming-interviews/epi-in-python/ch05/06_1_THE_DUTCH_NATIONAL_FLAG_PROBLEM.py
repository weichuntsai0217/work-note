from __future__ import print_function

def swap(x, i, j):
  temp = x[i]
  x[i] = x[j]
  x[j] = temp

def partition(x, pivot_idx):
  """
    Time complexity is O(n) where n is the length of x
    Because we have only three different numbers to sort,
    We can make a little twist for the "partition" of quicksort to sort this special case.
  """
  pivot = x[pivot_idx]
  i = -1
  for j in xrange(len(x)):
    if x[j] <= pivot:
      i += 1
      swap(x, i, j)
  end = i + 1
  m = -1
  for n in xrange(end):
    if x[n] < pivot: #  from 0 ~ end -1, there are only two different numbers, so we use "less than"
      m += 1
      swap(x, m, n)

def get_input(case=0):
  """
    From the problem's spec, we denote 0, 1, 2 as three different colors.
  """
  x = [0,1,2,0,1,2] if case < 3 else [2, 2, 1, 2, 0, 2, 1, 0, 2, 1, 0]
  if case == 0:
    return x, 0, [0, 0, 2, 1, 1, 2]
  elif case == 1:
    return x, 1, sorted(x)
  elif case == 2:
    return x, 2, [0, 1, 0, 1, 2, 2]
  elif case == 3:
    return x, 0, [1, 0, 1, 0, 1, 0, 2, 2, 2, 2, 2]
  elif case == 4:
    return x, 2, sorted(x)
  elif case == 5:
    return x, 4, [0, 0, 0, 2, 2, 2, 1, 2, 2, 1, 1]


def main():
  for arg in xrange(6):
    x, pivot_idx, ans = get_input(arg)
    partition(x, pivot_idx) # change x in-place
    print(x)
    print('Test success' if x == ans else 'Test failure')

if __name__ == '__main__':
  main()
