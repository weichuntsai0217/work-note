from __future__ import print_function

def get_min_messiness(words, line_len):
  """
    Time complexity is O(nL), where n is the number of words and L is the length of each line.
  """
  cache = [-1] * len(words)
  return min_messiness(len(words) - 1, words, line_len, cache)

def min_messiness(i, words, line_len, cache):
  # print('min_messiness is called.')
  if cache[i] != -1: return cache[i]
  left_len = line_len - len(words[i])
  min_j = 0
  for idx in xrange(i - 1, -1, -1):
    if left_len - (len(words[idx]) + 1) >= 0:
      left_len -= (len(words[idx]) + 1) # 1 for space
    else:
      min_j = idx + 1 # because we iterate words in reverse order.
      break
  if min_j == 0: # means the first i wors can be in one line.
    return left_len ** 2

  res = []
  residual = left_len
  for j in xrange(min_j, i+1):
    delta = 0
    if j > min_j:
      delta = len(words[j-1]) + 1
    residual += delta
    res.append(min_messiness(j-1, words, line_len, cache) + (residual ** 2))
  cache[i] = min(res)
  return cache[i]

def get_input(hard=False):
  if hard:
    return ['a'*3, 'b'*3, 'c', 'd', 'e'*2, 'f'*2, 'g'*7], 11, 36
  else:
    return ['a', 'b', 'c', 'd'], 5, 8

def main():
  for arg in [False, True]:
    words, line_len, ans = get_input(arg)
    expect = get_min_messiness(words, line_len)
    # print(words, line_len, ans)
    print(expect)
    print('Test success' if expect == ans else 'Test failure')

if __name__ == '__main__':
  main()
