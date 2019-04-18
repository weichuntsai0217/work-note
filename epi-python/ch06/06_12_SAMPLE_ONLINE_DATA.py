from __future__ import print_function

def sample_online_data(seq, k):
  """
    Still don't know what's the advantage of using this method. It looks like there is no difference betwenn this solution
    and 6.11
  """
  import random
  # Assume the seq has at least k items.
  res = []
  i = 0
  while i < k:
    try:
      x = seq.next()
      res.append(x)
      i += 1
    except StopIteration:
      break

  num_seen_so_far = k
  while True:
    try:
      x = seq.next()
      num_seen_so_far += 1
      idx_to_replace = random.randint(0, num_seen_so_far - 1)
      if idx_to_replace < k:
        res[idx_to_replace] = x
    except StopIteration:
      break

  return res
  
def get_input():
  return iter(range(10)), 3

def main():
  seq, k = get_input()
  res = sample_online_data(seq, k)
  print(res)
  

if __name__ == '__main__':
  main()
