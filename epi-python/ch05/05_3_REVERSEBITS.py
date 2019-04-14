from __future__ import print_function

def swap_bits(x, i, j):
  if (x >> i & 1) != (x >> j & 1):
    mask = (1 << i) | (1 << j)
    return x ^ mask
  return x

def reverse_bits(x):
  """
    The problem has assumed that x is 64-bit.
    The time complexity is O(32).
    In general, the time complexity is O(n / 2) fo n-bit integers (n is always the power of 2)
  """
  for i in xrange(32):
    x = swap_bits(x, i, 63 - i)
  return x


def get_cache():
  cache = []
  for x in xrange(2**16):
    res = x
    for i in xrange(8):
      res = swap_bits(res, i, 15 - i)
      # if x == 1: print(res)
    cache.append(res)
  return cache

cache = get_cache()

def reverse_bits_by_cache(x):
  """
    The problem has assumed that x is 64-bit.
    Assume cache exists, then the time complexity is O(1).
    In general, the time complexity is O(n / L) for n-bit integers and L-bit cache keys.
  """
  word_size = 16
  bit_mask = 0xffff
  return (
    cache[x & bit_mask] << (3 * word_size) |
    cache[(x >> word_size) & bit_mask] << (2 * word_size) |
    cache[(x >> (2*word_size)) & bit_mask] << (1 * word_size) |
    cache[(x >> (3*word_size)) & bit_mask]
  )



def get_input(big=False):
  if big:
    s = '10111'*12 + '0000'
    return int(s, 2), int(s[::-1], 2)
  s = '00000'*12 + '1111'
  return int(s, 2), int(s[::-1], 2)

def main():
  for arg in [False, True]:
    x, ans = get_input(arg)
    # res = reverse_bits(x)
    res = reverse_bits_by_cache(x)
    # print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
