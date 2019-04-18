from __future__ import print_function

def enumerate_prime_to_n(n):
  """
    Time complexity is O(nloglogn)
    Additional space complexity is O(n)
    This is the classic Sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).
    You can refer to http://www.csie.ntnu.edu.tw/~u91029/Prime.html for a detailed explaination.
    Don't forget that any composite number can be represented as the product of prime numbers.
  """
  size = (n-3)/2 + 1
  record = [True] * size
  primes = [2]
  for i in xrange(len(record)):
    if record[i]:
      p = 2 * i + 3
      primes.append(p)
      start = 2 * (i*i) + 6 * i + 3 # for kp where k < p is already sieved out by previous loops.
      delta = p
      # In prime space, we have to check p^2 + p, p^2 + 2p, ...etc.
      # However p^2 + p is even and is not in our record index mapping.
      # so in fact we have to check p^2 + 2p, p^2 + 4p , ...etc, and the corresponding index in record
      # is (p^2 - 3)/2 + 2p/2, (p^2 - 3)/2 + 4p/2 which is (p^2 - 3)/2 + p, (p^2 - 3)/2 + 2p, so delta shouble p.
      for j in xrange(start, size, delta):
        record[j] = False
  return primes

def get_input(case=0):
  n = None
  ans = None
  if case == 0:
    n = 18
    ans = [2,3,5,7,11,13,17]
  elif case == 1:
    n = 41
    ans = [2,3,5,7,11,13,17,19,23,29,31,37,41]

  return n, ans

def main():
  for case in xrange(2):
    n, ans = get_input(case)
    res = enumerate_prime_to_n(n)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
