from __future__ import print_function
# String format examle: print '{} {}'.format('one', 'two') => 'one two'

import sys
# Argument from command line example: sys.argv[1]

def count_bits(num):
  num_bits = 0
  while num != 0:
    num_bits += (num & 1)
    num >>= 1
  return num_bits

def main():
  arg = None
  if len(sys.argv) >= 2:
    arg = int(sys.argv[1])
  else:
    arg = 99
  print('Your input number is ', arg)
  print('The number of bits which are set to 1 is ', count_bits(arg))

if __name__ == '__main__':
  main()
