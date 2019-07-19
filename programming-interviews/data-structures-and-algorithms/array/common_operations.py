"""
  Use python 3.6.8
"""
import copy
from collections import deque

# Implement start
def rotate_in_place(array, shift):
  """
    HAS BUG
    Rotate an array in place with a right (positive) or left (negative) shift.
    The sign of shift for right or left follows the `collections.deque` tradition.
  """
  if not array: return []
  length = len(array)
  shift %= length # convert a left shift (negative) into a right shift (positive)
  if shift == 0:
    return
  if (shift == 1) or length % shift:
    src_idx = 0
    src_val = array[src_idx]
    for i in range(len(array)):
      dst_idx = src_idx + shift if (src_idx + shift) < length else (src_idx + shift - length)
      dst_val = array[dst_idx]
      array[dst_idx] = src_val
      src_idx = dst_idx
      src_val = dst_val
  else:
    groups = length // shift
    for i in range(shift):
      src_idx = i
      src_val = array[src_idx]
      for j in range(groups):
        dst_idx = src_idx + shift if (src_idx + shift) < length else (src_idx + shift - length)
        dst_val = array[dst_idx]
        array[dst_idx] = src_val
        src_idx = dst_idx
        src_val = dst_val

def rotated_with_copy_by_allocating(array, shift, start=None, end=None):
  """
    The space complexity including the output is O(n) where n is the array length.
    Copy and rotate an array with a right (positive) or left (negative) shift.
    The sign of shift for right or left follows the `collections.deque` tradition.
  """
  if not array: return []
  if not (isinstance(start, int) and isinstance(end, int) and start < end):
    start = 0
    end = len(array)
  length = end - start
  shift %= length # convert a left shift (negative) into a right shift (positive).

  res = [None] * len(array)
  for i in range(start):
    res[i] = array[i]
    
  for i in range(start, end):
    dst_idx = i + shift if (i + shift) < end else (i + shift - length)
    res[dst_idx] = array[i]

  for i in range(end, len(array)):
    res[i] = array[i]
  return res
  
def rotated_with_copy_by_slicing(array, shift, start=None, end=None): # end = start + len(subarray_you_want_to_rotate)
  """
    The space complexity including the output is O(n) where n is the array length.
    Copy and rotate an array with a right (positive) or left (negative) shift.
    The sign of shift for right or left follows the `collections.deque` tradition.
  """
  if not array: return []
  if not (isinstance(start, int) and isinstance(end, int) and start < end):
    start = 0
    end = len(array)
  length = end - start
  shift = (-shift) % length # convert a left shift (negative) into a right shift (positive)
  """
  The slicing behavior is opposite to `collections.deque`, so we give it a negative sign in the above line.
  """
  subarray = array[start:end]
  subarray = subarray[shift:] + subarray[:shift]
  return array[:start] + subarray + array[end:]

def remove_duplicates_in_place_for_sorted_array(array, trim=False):
  """
    The time complexity is O(n)
    The space complexity including the output is O(1)
  """
  if not array: return 0
  write_idx = 1
  for i in range(1, len(array)):
    if array[i] != array[write_idx-1]:
      array[write_idx] = array[i]
      write_idx += 1
  if trim:
    delta = len(array) - write_idx
    for i in range(delta):
      array.pop()
  return write_idx # write_idx is also the effective length of the array after duplicates are removed.

def remove_duplicates_with_copy_for_sorted_array(array):
  """
    The time complexity is O(n)
    The space complexity including the output is O(n)
  """
  if not array: return []
  res = [array[0]]
  for i in range(1, len(array)):
    if array[i] != res[-1]:
      res.append(array[i])
  return res

def remove_duplicates_for_unsorted_array_in_place(array):
  """
    The time complexity is O(n) where n is the array length
    The space complexity including the output is O(n) where n is the array length.
    We focus on immutable items (str or int) in an array,
    so we can use `set()` to record them.
  """
  if not array: return 0
  seen = set([array[0]]) # the item we've seen
  write_idx = 1
  for i in range(1, len(array)):
    if array[i] not in seen:
      array[write_idx] = array[i]
      seen.add(array[i])
      write_idx += 1
  return write_idx # write_idx is also the effective length of the array after duplicates are removed.

def remove_duplicates_for_unsorted_array_with_copy(array):
  """
    The time complexity is O(n) where n is the array length
    The space complexity including the output is O(2n) where n is the array length.
    We focus on immutable items (str or int) in an array,
    so we can use `set()` to record them.
  """
  if not array: return []
  seen = set() # the item we've seen
  res = []
  for item in array:
    if item not in seen:
      res.append(item)
      seen.add(item)
  return res

def merge_two_sorted_arrays(a, b):
  """
    The space complexity including the output is O(n) where n is the array length.
  """
  i = 0
  j = 0
  res = []
  while True:
    if i < len(a) and j < len(b):
      if a[i] <= b[j]:
        res.append(a[i])
        i += 1
      else:
        res.append(b[j])
        j += 1
    elif i < len(a):
      res += a[i:]
      i = len(a)
    elif j < len(b):
      res += b[j:]
      j = len(b)
    else:
      break
  return res

def merge_two_adjacent_subarrays_in_a_src_array(src, p, q, r):
  """
    The implement is from page 31 of Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
    This function is usually used in merge sort.
    The first subarray is from p ~ q (inclusive)
    and the second subarray is from q + 1 ~ r (inclusive)
    The space complexity including the output is O(r - p + 1).
  """
  left = src[p:q+1]
  left.append(float('inf')) # use 'inf' as a sentinel to make edge case much easier
  right = src[q+1:r+1]
  right.append(float('inf')) # use 'inf' as a sentinel to make edge case much easier
  i = 0
  j = 0
  for k in range(p, r+1):
    if left[i] <= right[j]:
      src[k] = left[i]
      i += 1
    else:
      src[k] = right[j]
      j += 1

def is_palindromic(src, start=None, end=None): # the subarray we want to check is from start ~ end (inclusive)
  """
    Check if an array/string is palindromic.
    The time complexity is O(end - start + 1) = O(end - start).
    The space complexity without output is O(1).
  """
  if not (isinstance(start, int) and isinstance(end, int) and start <= end):
    start = 0
    end = len(src) - 1
  i = start
  j = end
  while i < j:
    if src[i] != src[j]:
      return False
    i += 1
    j -= 1
  return True

def reverse_in_place(array, start=None, end=None): # the subarray we want to reverse is from start ~ end (inclusive)
  """
    Reverse an array in place.
    The space complexity including output is O(1).
  """
  """
    The simplest way to reverse the whole array in-place is:
    ```
    array.reverse()
    ```
    But this built-in function does not accept any arguments to assign a subarray to reverse.
  """
  if not (isinstance(start, int) and isinstance(end, int) and start <= end):
    start = 0
    end = len(array) - 1
  i = start
  j = end
  while i < j:
    array[i], array[j] = array[j], array[i]
    i += 1
    j -= 1

def reverse_with_copy(array, start=None, end=None): # the subarray we want to reverse is from start ~ end (inclusive)
  """
    Copy and reverse an array.
    The space complexity including output is O(n).
  """
  """
    The simplest way to reverse the whole array with a copy is:
    ```
    new_array = array[::-1]
    ```
    or
    ```
    new_array = list(reversed(array))
    ```
    But these built-in ways do not accept any arguments to assign a subarray to reverse.
  """
  copy_array = array[:]
  reverse_in_place(copy_array, start, end)
  return copy_array

def partition(array, p, r): # the subarray we want to reverse is from start ~ end (inclusive)
  """
    The implement is from page 31 of Thomas H. Cormen et al., "Introduction to Algorithms, 3rd" (2009).
    This algorithm can be used in
    1. quick sort
    2. sorting an array with 3 kind of items (you just do partition twice.)
  """
  x = array[r] # always choose the last item of the subarray as pivot
  i = p - 1
  for j in range(p, r):
    if array[j] <= x:
      i += 1
      array[i], array[j] = array[j], array[i] # python's way to swap
  array[i+1], array[r] = array[r], array[i+1]
  return i + 1

# Implement end

# Test utils start
def get_shift_from_deque(array, shift, start=None, end=None): # end = start + len(subarray_you_want_to_rotate)
  if not (isinstance(start, int) and isinstance(end, int) and start < end):
    start = 0
    end = len(array)
  prefix = array[:start]
  middle_q = deque(array[start:end])
  suffix = array[end:]
  middle_q.rotate(shift)
  return prefix + list(middle_q) + suffix

def test_partition():
  def get_inputs(case):
    array = [5, 6, 3, 1, 2, 1, 3, 4, 6, 3, 4]
    p = 0
    r = len(array) - 1
    ans_pivot_idx = 7
    ans_array = [3, 1, 2, 1, 3, 4, 3, 4, 6, 5, 6]
    if case == 0:
      pass
    elif case == 1:
      array = [6, 6, 4, 2, 3, 4, 1, 3, 1, 5, 3]
      ans_pivot_idx = 5
      ans_array = [2, 3, 1, 3, 1, 3, 4, 6, 6, 5, 4]
    elif case == 2:
      prefix = list('abc')
      suffix = list('de')
      array = prefix + [6, 6, 4, 2, 3, 4, 1, 3, 1, 5, 3] + suffix
      p = len(prefix)
      r = len(array) - len(suffix) - 1
      ans_pivot_idx = 5 + len(prefix)
      ans_array = prefix + [2, 3, 1, 3, 1, 3, 4, 6, 6, 5, 4] + suffix
      
    return array, p, r, ans_pivot_idx, ans_array
  for case in range(3):
    array, p, r, ans_pivot_idx, ans_array = get_inputs(case)
    pivot_idx = partition(array, p, r)
    assert pivot_idx == ans_pivot_idx
    assert array == ans_array
  print('partition success')

def test_rotated_with_copy_fns(fn):
  def test_case_a(src_rng, rotate_rng):
    src_ary = list(src_rng)
    array = src_ary[:]
    for i in rotate_rng:
      res = fn(array, i)
      ans = get_shift_from_deque(array, i)
      assert src_ary == array
      assert res == ans

  def test_case_b(src_rng, rotate_rng, start, end):
    src_ary = list(src_rng)
    array = src_ary[:]
    for i in rotate_rng:
      res = fn(array, i, start, end)
      ans = get_shift_from_deque(array, i, start, end)
      assert src_ary == array
      assert res == ans

  test_case_a(range(1, 5), range(-9, 10))
  test_case_a(range(1, 8), range(-15, 16))
  test_case_a(range(1, 16), range(-30, 31))

  test_case_b(range(1, 5), range(-9, 10), 0, 2)
  test_case_b(range(1, 5), range(-9, 10), 1, 3)
  test_case_b(range(1, 5), range(-9, 10), 2, 4)
  test_case_b(range(1, 8), range(-15, 16), 0, 3)
  test_case_b(range(1, 8), range(-15, 16), 2, 5)
  test_case_b(range(1, 8), range(-15, 16), 4, 7)
  test_case_b(range(1, 16), range(-30, 31), 0, 5)
  test_case_b(range(1, 16), range(-30, 31), 4, 9)
  test_case_b(range(1, 16), range(-30, 31), 11, 15)

  print('{} success'.format(fn.__name__))

def test_rotate_in_place():
  def test_case(src_rng, rotate_rng):
    src_ary = list(src_rng)
    for i in rotate_rng:
      res = copy.deepcopy(src_ary)
      rotate_in_place(res, i)
      ans = get_shift_from_deque(src_ary, i)
      try:
        assert res == ans
      except AssertionError:
        print('i =', i)
        print('i % len =', i % len(res))
        print('res =', res)
        print('ans =', ans)
        raise AssertionError

  test_case(range(1, 5), range(-9, 10))
  test_case(range(1, 8), range(-15, 16))
  test_case(range(1, 16), range(-30, 31))
  print('rotate success')

def get_test_data_for_remove_duplicates_for_unsorted_array_fns(case, trim=False):
  array = []
  ans_write_idx = 0
  ans_array = []
  if case == 0:
    pass
  elif case == 1:
    array = [1]
    ans_write_idx = 1
    ans_array = [1]
  elif case == 2:
    array = [3, 3, 6, 2, 3, 1, 4, 4, 1, 5]
    ans_write_idx = 6
    ans_array =[3, 6, 2, 1, 4, 5, 4, 4, 1, 5]
    if trim: ans_array = ans_array[:6]
  elif case == 3:
    array = [3, 3, 6, 2, 1, 4, 1, 4, 3, 5, 6]
    ans_write_idx = 6
    ans_array = [3, 6, 2, 1, 4, 5, 1, 4, 3, 5, 6]
    if trim: ans_array = ans_array[:6]
  return array, ans_write_idx, ans_array

def test_remove_duplicates_for_unsorted_array_in_place():
  for case in range(4):
    array, ans_write_idx, ans_array = get_test_data_for_remove_duplicates_for_unsorted_array_fns(case)
    write_idx = remove_duplicates_for_unsorted_array_in_place(array)
    assert write_idx == ans_write_idx
    assert array == ans_array
  print('remove_duplicates_for_unsorted_array_in_place success')

def test_remove_duplicates_for_unsorted_array_with_copy():
  for case in range(4):
    array, ans_write_idx, ans_array = get_test_data_for_remove_duplicates_for_unsorted_array_fns(case, True)
    src_check = array[:]
    res = remove_duplicates_for_unsorted_array_with_copy(array)
    assert array == src_check
    assert res == ans_array
  print('remove_duplicates_for_unsorted_array_with_copy success')

def get_test_data_for_remove_duplicates_for_sorted_array_fns(case):
  array = []
  trim = False
  ans_write_idx = 0
  ans_array = []
  if case == 0:
    pass
  elif case == 1:
    trim = True
  elif case == 2:
    array = [1]
    ans_write_idx = 1
    ans_array = [1]
  elif case == 3:
    array = [1]
    trim = True
    ans_write_idx = 1
    ans_array = [1]
  elif case == 4:
    array = [1,1,2,3,3,3,4,4,5,6]
    ans_write_idx = 6
    ans_array = [1,2,3,4,5,6,4,4,5,6]
  elif case == 5:
    array = [1,1,2,3,3,3,4,4,5,6]
    trim = True
    ans_write_idx = 6
    ans_array = [1,2,3,4,5,6]
  elif case == 6:
    array = [1,1,2,3,3,3,4,4,5,6,6]
    ans_write_idx = 6
    ans_array = [1,2,3,4,5,6,4,4,5,6,6]
  elif case == 7:
    array = [1,1,2,3,3,3,4,4,5,6]
    trim = True
    ans_write_idx = 6
    ans_array = [1,2,3,4,5,6]
  
  return array, trim, ans_write_idx, ans_array

def test_remove_duplicates_in_place_for_sorted_array():
  for case in range(8):
    array, trim, ans_write_idx, ans_array = get_test_data_for_remove_duplicates_for_sorted_array_fns(case)
    write_idx = remove_duplicates_in_place_for_sorted_array(array, trim)
    assert write_idx == ans_write_idx
    assert array == ans_array
  print('remove_duplicates_in_place_for_sorted_array success')

def test_remove_duplicates_with_copy_for_sorted_array():
  for case in [1, 3, 5, 7]:
    array, trim, ans_write_idx, ans_array = get_test_data_for_remove_duplicates_for_sorted_array_fns(case)
    src_check = array[:]
    res_array = remove_duplicates_with_copy_for_sorted_array(array)
    assert res_array == ans_array
    assert array == src_check
  print('remove_duplicates_with_copy_for_sorted_array success')

def get_test_data_fn_for_merge_fns(adjacent=False):
  def get_inputs(case):
    a = []
    b = []
    if case == 0:
      pass
    elif case == 1:
      a = [1, 2]
    elif case == 2:
      b = [1, 2]
    elif case == 3:
      a = [1, 2, 3]
      b = [1, 2, 3]
    elif case == 4:
      a = [1, 3, 5, 7, 9]
      b = [2, 4, 6]
    elif case == 5:
      a = [2, 4, 6]
      b = [1, 3, 5, 7, 9]
    elif case == 6:
      a = [1, 1, 2, 4, 6, 6, 8, 8, 10, 10]
      b = [2, 3, 3, 5, 6, 7, 8, 8]
    elif case == 7:
      a = [2, 3, 3, 5, 6, 7, 8, 8]
      b = [1, 1, 2, 4, 6, 6, 8, 8, 10, 10]
    ans = sorted(a + b)
    return a, b, ans

  def get_adjacent_inputs(case):
    a, b, ans = get_inputs(case)
    prefix = list('abc')
    suffix = list('def')
    if case <= 4:
      prefix = []
      suffix = []
    src = prefix + a + b + suffix
    p = len(prefix)
    q = len(prefix) + len(a) - 1
    r = len(prefix) + len(a) + len(b) - 1
    ans = prefix + ans + suffix
    return src, p, q, r, ans

  if adjacent:
    return get_adjacent_inputs
  return get_inputs
    

def test_merge_two_sorted_arrays():
  get_inputs = get_test_data_fn_for_merge_fns()
  for i in range(8):
    a, b, ans = get_inputs(i)
    res = merge_two_sorted_arrays(a, b)
    assert res == ans
  print('merge_two_sorted_arrays success')

def test_merge_two_adjacent_subarrays_in_a_src_array():
  get_inputs = get_test_data_fn_for_merge_fns(True)
  for i in range(8):
    res, p, q, r, ans = get_inputs(i)
    merge_two_adjacent_subarrays_in_a_src_array(res, p, q, r)
    assert res == ans
  print('merge_two_adjacent_subarrays_in_a_src_array success')

def get_test_data_for_reverse_fns(case):
  array = []
  start = None
  end = None
  ans = []
  if case == 0:
    pass
  elif case == 1:
    array = [0]
    ans = [0]
  elif case == 2:
    array = list(range(5))
    ans = list(reversed(array))
  elif case == 3:
    array = list(range(5))
    start = 0
    end = 2
    ans = [2, 1, 0, 3, 4]
  elif case == 4:
    array = list(range(5))
    start = 2
    end = 4
    ans = [0, 1, 4, 3, 2]
  elif case == 5:
    array = list(range(5))
    start = 1
    end = 3
    ans = [0, 3, 2, 1, 4]
  return array, start, end, ans

def test_reverse_in_place():
  for case in range(6):
    res, start, end, ans = get_test_data_for_reverse_fns(case)
    reverse_in_place(res, start, end)
    assert res == ans
  print('reverse_in_place success')

def test_reverse_with_copy():
  for case in range(6):
    array, start, end, ans = get_test_data_for_reverse_fns(case)
    src_check = array[:]
    res = reverse_with_copy(array, start, end)
    assert res == ans
    assert src_check == array
  print('reverse_with_copy success')

def test_is_palindromic():
  def get_inputs(case):
    src = list('')
    start = None
    end = None
    ans = True
    prefix = list('123')
    suffix = list('456')
    if case == 0:
      pass
    elif case == 1:
      src = list('a')
      ans = True
    elif case == 2:
      src = list('abccba')
      ans = True
    elif case == 3:
      src = list('qsedxdesq')
      ans = True
    elif case == 4:
      src = list('ab')
      ans = False
    elif case == 5:
      src = list('abcxba')
      ans = False
    elif case == 6:
      src = list('qsedxrdesq')
      ans = False
    elif case == 7:
      middle = list('a')
      ans = True
      src = prefix + middle + suffix
      start = len(prefix)
      end = len(prefix) + len(middle) - 1
    elif case == 8:
      middle = list('abccba')
      ans = True
      src = prefix + middle + suffix
      start = len(prefix)
      end = len(prefix) + len(middle) - 1
    elif case == 9:
      middle = list('qsedxdesq')
      ans = True
      src = prefix + middle + suffix
      start = len(prefix)
      end = len(prefix) + len(middle) - 1
    elif case == 10:
      middle = list('ab')
      ans = False
      src = prefix + middle + suffix
      start = len(prefix)
      end = len(prefix) + len(middle) - 1
    elif case == 11:
      middle = list('abcxba')
      ans = False
      src = prefix + middle + suffix
      start = len(prefix)
      end = len(prefix) + len(middle) - 1
    elif case == 12:
      middle = list('qsedxrdesq')
      ans = False
      src = prefix + middle + suffix
      start = len(prefix)
      end = len(prefix) + len(middle) - 1
    return src, start, end, ans
  for case in range(13):
    src, start, end, ans = get_inputs(case)
    assert is_palindromic(src, start, end) == ans
  print('is_palindromic success')

# Test utils end

def main():
  # test_rotate_in_place()
  test_rotated_with_copy_fns(rotated_with_copy_by_slicing)
  test_rotated_with_copy_fns(rotated_with_copy_by_allocating)
  test_remove_duplicates_in_place_for_sorted_array()
  test_remove_duplicates_with_copy_for_sorted_array()
  test_remove_duplicates_for_unsorted_array_in_place()
  test_remove_duplicates_for_unsorted_array_with_copy()
  test_merge_two_sorted_arrays()
  test_merge_two_adjacent_subarrays_in_a_src_array()
  test_reverse_in_place()
  test_reverse_with_copy()
  test_is_palindromic()
  test_partition()

if __name__ == '__main__':
  main()
