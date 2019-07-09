from __future__ import print_function
import heapq
import math

def get_priority(x, y, z):
  """
    The negative sign because python has only min heap.
  """
  return -math.sqrt(x**2 + y**2 + z**2)

def compute_the_k_closest_starts(stars, k):
  """
    The time complexity is O(n * logk) where n is the number elements in stars and k is the problem's requirement.
    The additional space is O(k) because we cached k priorities (negative distance) for heap push.
  """
  it = iter(stars) # mimic data in the file.
  max_heap = []
  for i in xrange(k):
    try:
      [idx, x, y, z] = it.next() # idx is just the name or id of the star to make test more easy.
      pri = get_priority(x, y, z)
      heapq.heappush(max_heap, [pri, idx, x, y, z])
    except StopIteration:
      break

  while True:
    try:
      [idx, x, y, z] = it.next()
      pri = get_priority(x, y, z)
      heapq.heappushpop(max_heap, [pri, idx, x, y, z])
    except StopIteration:
      break

  return map(lambda x: [x[1], x[2], x[3], x[4]], sorted(max_heap, reverse=True))

def get_input(case=0):
  import random
  stars = []
  k = None
  ans = []
  if case == 0:
    for i in xrange(16):
      stars.append([chr(ord('a') + i), i+1, i+1, i+1])
    stars = sorted(stars, key=lambda x: random.random())
    k = 8
    ans = sorted(stars, key=lambda star: math.sqrt(star[1]**2 + star[2]**2 + star[3]**2))[:k]
  return stars, k, ans

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    stars, k, ans = get_input(case)
    print('Input:')
    print('stars =', stars)
    print('k =', k)
    res = compute_the_k_closest_starts(stars, k)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
