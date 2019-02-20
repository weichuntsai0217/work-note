from __future__ import print_function

def find_decomposition_of_words(domain, words): # words is a set object.
  """
    Time complexity: O(n^2 * W), n is the length of domain string and W is the length of the longest word in words.
  """
  if not domain or not words: return []

  last_length = [-1] * len(domain)
  for i in xrange(len(domain)):
    prefix = domain[0:i+1]
    if prefix in words:
      last_length[i] = i + 1
    
    if last_length[i] == -1:
      for j in xrange(i):
        if last_length[j] != -1 and domain[j+1:i+1] in words:
          last_length[i] = i - j
          break

  res = []
  if last_length[-1] != -1:
    i = len(last_length) - 1
    while i >= 0:
      start = i - last_length[i]
      res.insert(0, domain[start+1:i+1])
      i = start

  return res

def get_input(hard=False):
  domain = None
  words = None
  if hard:
    domain = 'amanaplanacanal'
    words = set(['a', 'man', 'a', 'plan', 'a', 'canal'])
    ans = ['a', 'man', 'a', 'plan', 'a', 'canal']
  else:
    domain = 'addbad'
    words = set(['a', 'add', 'bad'])
    ans = ['add', 'bad']
  return domain, words, ans

def main():
  for arg in [False, True]:
    domain, words, ans = get_input(arg)
    print('Test success' if find_decomposition_of_words(domain, words) == ans else 'Test failure')


if __name__ == '__main__':
  main()
