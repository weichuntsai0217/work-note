from __future__ import print_function
# String format examle: print '{} {}'.format('one', 'two') => 'one two'

import sys
# Argument from command line example: sys.argv[1]

def your_function():
  print('{} {}'.format('one', 'two'), 'three')

def main():
  your_function()

if __name__ == '__main__':
  main()
