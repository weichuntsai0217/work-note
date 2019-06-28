import concurrent.futures

def worker(lower, upper):
  for i in range(lower, upper + 1):
    assert collatz_check(i, set())
  print('{} - {} is successful'.format(lower, upper))

def collatz_check(n, visited):
  """
    We cannot cache known results like we did in problem 12.11 on page 188 of EPI in python.
    Because on multi-thread environment, to test n, we can not guarantee that we know the result of 1 ~ (n - 1)
    when we want to test n.
    For example, we have 2 threads and we want to check first n = 32 for collatz conjecture.
    Let's say test 1 ~ 16 on thread 1 and test 17 ~ 32 on thread 2.
    When thread 2 tries to test 32, and you use the solution of 12.11, you would find out that
    your known result cache does not contain 16 (because thread 2 does not check 16.)

    Please be careful that the single threaded algorithm could be changed in the case of multi threads.
  """
  if n == 1:
    return True
  if n in visited:
    return False
  visited.add(n)
  if n & 1:
    return collatz_check(3 * n + 1, visited)
  return collatz_check(n // 2, visited)

def main():
 NTHREADS = 4
 range_size = 7
 n = 35
 with concurrent.futures.ThreadPoolExecutor(max_workers=NTHREADS) as executor:
   remainder = n % range_size
   tot_groups = n // range_size + (1 if remainder else 0)
   for i in range(tot_groups):
      lower = i * range_size + 1
      upper = (i + 1) * range_size
      if (i == (tot_groups - 1)) and (remainder != 0):
        upper = lower + remainder - 1
      executor.submit(worker, lower, upper)
 

if __name__ == '__main__':
  main()


