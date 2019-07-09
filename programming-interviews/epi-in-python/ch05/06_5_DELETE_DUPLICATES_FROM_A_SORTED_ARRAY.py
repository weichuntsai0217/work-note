from __future__ import print_function

def swap(x, i, j):
  temp = x[i]
  x[i] = x[j]
  x[j] = temp

def delete_duplicates_of_sorted_array(x):
  if not x: return 0

  write_idx = 1
  for i in xrange(1, len(x)):
    # the key point is that write_idx - 1 is the distinct data you write last time.
    if x[write_idx - 1] != x[i]:
      x[write_idx] = x[i]
      write_idx += 1
  return write_idx


def get_input(case=0):
  if case == 0:
    x = [2]
    return x, x, len(x)
  elif case == 1:
    x = [1,1,2,2,3,3]
    return x, [1,2,3,None,None,None], 3
  elif case == 2:
    x = [2,3,5,5,7,11,11,11,13]
    return x, [2,3,5,7,11,13,None,None,None], 6

def main():
  for arg in xrange(3):
    x, ans_x, ans_l = get_input(arg)
    l = delete_duplicates_of_sorted_array(x)
    print(x[0:l])
    print(l)
    print('Test success' if x[:l] == ans_x[:ans_l] and l == ans_l else 'Test failure')

if __name__ == '__main__':
  main()
