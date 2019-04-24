from __future__ import print_function

def trivial_replace_and_remove(size, s):
  """
    The time complexity is O(n)
    The additional space complexity is O(n) (including output)
  """
  res = []
  source = s[:size]
  for c in source:
    if c == 'a':
      res.append('d')
      res.append('d')
    elif c != 'b':
      res.append(c)
  return len(res), res

def replace_and_remove(size, s): # s is a character array
  """
    Here we assume the number of 'b' is greater than or equal to the number of 'a' to prevent index out of range.
    The time complexity is O(n)
    The additional space complexity is O(1) (including output)
  """
  write_idx = 0
  a_count = 0
  for i in xrange(size):
    """
      if size = 5, that means we only handle the top 5 elements in the array.
      write_idx is the position to write.
      The elements before write_idx are all done (no need to move).
      i is use to traverse every element.
      a_count is used to record how many 'a' we get.
      The key part is that we keep i = write_idx until we meet s[i] = 'b', each time we get s[i] = 'b',
      we stop increment write_idx and we just increment i, so at the beginning of each loop
      (i - write_idx) means the number of 'b' before position i.
      For example, if there are 3 'b' before the current position i, then what we want to do is either
        1. if s[i] is not a 'b' s[i] should be moved to i - (i - write_idx) = write_idx.
           And after the move, write_idx += 1 (i would be incremented automatically by the loop)
        2. if s[i] is a 'b' then don't move s[i], keep i going until i meets an elemente which is not a 'b'.
      Ex: 'abcebba' -> 'aceabba', the number of 'b' before 'ce' is 1, so 'ce' only needs to move 1 step to the left;
           however, for the last 'a', the last 'a' needs to move 3 steps to the left
           because there are total 3 'b' before the last 'a'.
    """
    if s[i] != 'b':
      s[write_idx] = s[i]
      write_idx += 1
    if s[i] == 'a':
      a_count += 1
  """
    Now at this time point, write_idx is just the length of the original top 'size' array which deleted 'b'
    Ex: 'abcebbaxxxa' and size = 7 (only handle the top 7 elements) -> 'aceabbaxxx' write_idx = 4 a_count = 2
        Now we just focus on 'aceabb' because write_idx = 4 a_count = 2
  """
  cur_idx = write_idx - 1
  """
    cur_idx is the last index of the array 'acea' we just handled, cur_idx now point to the last 'a'.
  """
  
  write_idx = write_idx + a_count - 1
  """
    Every 'a' would increase the final array length by 1,
    Now the array we want to handle is 'aceabb' and write_idx point to the last 'b'.
          
          write_idx = 5
          |
    'aceabb'
        |
        cur_idx = 3

    From now on, we are working our way backwards and
    the key point is that the range from cur_idx + 1 to write_idx (including write_idx)
    is the buffer zone you can safely write and the elements after write_idx are all moved done.
    write_idx - cur_idx = the number of 'a' which is not replaced by 'd'.
    Everytime when s[cur_idx] is a 'a', the distance between write_idx and cur_idx would be decreased
    otherwise the distance would keep the same,
    so you don't worry about if there is any element is replaced before it is moved to the right of write_idx.
  """
  
  final_size = write_idx + 1 # trivial

  while cur_idx >= 0:
    if s[cur_idx] == 'a':
      s[write_idx] = 'd'
      write_idx -= 1
      s[write_idx] = 'd'
      write_idx -= 1
    else:
      s[write_idx] = s[cur_idx]
      write_idx -= 1
    cur_idx -= 1

  return final_size

def get_input(case=0):
  size = None
  ary = None
  ans_size = None
  ans_ary = None
  
  if case == 0:
    size = 3
    ary = list('bbebf')
    ans_size = 1
    ans_ary = list('e')
  elif case == 1:
    size = 7
    ary = list('abcebbaxxxa')
    ans_size = 6
    ans_ary = list('ddcedd')
  elif case == 2:
    size = 7
    ary = list('acdbbca')
    ans_size = 7
    ans_ary = list('ddcdcdd')
  return size, ary, ans_size, ans_ary

def main():
  print('Use replace_and_remove')
  for case in xrange(3):
    size, ary, ans_size, ans_ary = get_input(case)
    res_size = replace_and_remove(size, ary) # ary has bee modified.
    print(res_size)
    print(ary[:res_size])
    print('Test success' if (res_size == ans_size) and (ary[:res_size] == ans_ary) else 'Test failure')

  print('==========')
  print('Use trivial_replace_and_remove')
  for case in xrange(3):
    size, ary, ans_size, ans_ary = get_input(case)
    res_size, res_ary = trivial_replace_and_remove(size, ary)
    print(res_size)
    print(res_ary)
    print('Test success' if (res_size == ans_size) and (res_ary == ans_ary) else 'Test failure')

if __name__ == '__main__':
  main()
