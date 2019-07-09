from __future__ import print_function

def increnment(mapping, w):
  if w not in mapping:
    mapping[w] = 0
  mapping[w] += 1

def find_index(sentence, freq, start, m, n):
  used_w_freq = {}
  for i in xrange(m):
    cur_w = sentence[start + i*n : start + (i+1)*n]
    if cur_w not in freq:
      return False
    increnment(used_w_freq, cur_w)
    if used_w_freq[cur_w] > freq[cur_w]:
      return False
  return True

def compute_all_string_decompositions_epi(sentence, words):
  """
    The time complexity is O(Nmn) where m is the number of words and n is the length of each word and
    N is the sentence length.
    The additional space complexity is O(m).
  """
  freq = {}
  for w in words:
    increnment(freq, w)
  
  m = len(words)
  n = len(words[0])
  res = []
  for i in xrange(len(sentence) - m*n + 1):
    if find_index(sentence, freq, i, m, n):
      res.append(i)
  return res


def recursive_comb(words, used, prefix, res):
  if len(prefix) == len(words) * len(words[0]):
    res.append(prefix)
    return
  for i in xrange(len(words)):
    if not used[i]:
      used[i] = True
      new_prefix = prefix + words[i]
      recursive_comb(words, used, new_prefix, res)
      used[i] = False

def compute_all_string_decompositions(sentence, words):
  """
    The time complexity is O( (m!)N(mn) + (m!)mn) where m is the number of words and n is the length of each word and
    N is the sentence length.
    The additional space complexity is O( (m!)mn )
  """
  used = [False] * len(words)
  combs = []
  recursive_comb(words, used, '', combs)

  res = []
  for comb in combs:
    for i in xrange(len(sentence) - len(combs[0]) + 1):
      if sentence.startswith(comb, i):
        res.append(i)
  return res


def get_input(case=0):
  sentence = 'amanaplanacanal'
  words = ['can', 'apl', 'ana']
  ans = [4]
  if case == 0:
    pass
  elif case == 1:
    sentence = 'aabbccbbaabbbbaacc'
    words = ['aa', 'bb', 'cc']
    ans = [0, 4, 12]
  elif case == 2:
    sentence = 'aabbccbbaabbbbaacc'
    words = ['aa', 'bb', 'cc', 'dd']
    ans = []
  return sentence, words, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    print('Input:')
    sentence, words, ans = get_input(case)
    print('sentence =', sentence)
    print('words =', words)
    res = sorted(compute_all_string_decompositions_epi(sentence, words))
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

