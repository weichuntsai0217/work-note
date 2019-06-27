"""
  These warmup examples are from page 26 of Elements of Programming Interviews
"""

from __future__ import print_function


def get_lowest_one_mask(x):
  """
    Example numbers here are represented by binary digit.
    if x is 11010 then  x & (~(x-1)) is 10
  """
  return x & (~(x-1))

def replace_lowest_one_with_zero(x):
  """
    Example numbers here are represented by binary digit.
    if x is 11010 then  x & (x-1) is 11000
  """
  return x & (x-1)

def is_power_of_2(x):
  """
    If x is power of 2, it must be equal to its lowest_one_mask.
  """
  return x == get_lowest_one_mask(x)

def mod_power_of_2(x, y):
  """
    y must be power of 2, ex: y = 2**6 = 64
  """
  mask = y - 1
  return x & mask

def set_rightmost_zeros_to_one(x):
  mask = get_lowest_one_mask(x) - 1
  return x | mask


def main():
  x = int('11010', 2)
  print('Test get_lowest_one_mask:')
  print(get_lowest_one_mask(x) == 2)

  print('Test replace_lowest_one_with_zero:')
  print(replace_lowest_one_with_zero(x) == 24)

  print('Test is_power_of_2:')
  flag = True
  for arg in [1, 2, 4, 8, 16, 32, 64, 128, 65536]:
    if not is_power_of_2(arg):
      flag = False
      break
  print(flag)
  
  print('Test mod_power_of_2:')
  print(mod_power_of_2(77, 64) == (77 % 64))
  print(mod_power_of_2(77, 65536) == 77)
  print(mod_power_of_2(178321347, 65536) == (178321347 % 65536))

  print('Test set_rightmost_zeros_to_one:')
  x = int('01010000', 2)
  y = int('01011111', 2)
  print(set_rightmost_zeros_to_one(x) == y)

if __name__ == '__main__':
  main()
