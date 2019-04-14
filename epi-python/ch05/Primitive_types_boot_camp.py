from __future__ import print_function

def count_bits(num):
  num_bits = 0
  while num != 0:
    num_bits += (num & 1)
    num >>= 1
  return num_bits

def get_input(hard=False):
  if hard:
    return 99, 4
  return 6, 2

def main():
  for arg in [False, True]:
    num, ans = get_input(arg)
    res = count_bits(num)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
