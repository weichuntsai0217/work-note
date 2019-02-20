from __future__ import print_function

def get_longest_nondec_seq_len(seq):
  """
    Time complexity is O(n^2), where n is the number of elements in seq.
  """
  if not seq: return 0
  len_list = [1] + [0] * (len(seq) - 1)
  for i in xrange(1, len(seq)):
    for j in xrange(i):
      if seq[j] < seq[i]:
        len_list[i] = max(1 + len_list[j], len_list[i])
  return max(len_list)

def get_input(hard=False):
  if hard:
    pass
  else:
    return [0, 8, 4, 12, 2, 10, 6, 14, 1, 9], 4

def main():
  for arg in [False]:
    seq, ans = get_input(arg)
    expect = get_longest_nondec_seq_len(seq)
    print(expect)
    print('Test success' if expect == ans else 'Test failure')

if __name__ == '__main__':
  main()
