from __future__ import print_function

def find_min_squential_cover_epi(words, keywords):
  """
    From the problem's spec, now keywords are all distinct.
    The time complexity is O(n)
    The additional space complexity is O(m) where m is the number of keywords.
  """
  key_to_index = {}
  last_occurrence = []
  shortest_lens_flo = [] # lo means "from last last_occurrence"
  for i in xrange(len(keywords)):
    key_to_index[keywords[i]] = i
    last_occurrence.append(-1)
    shortest_lens_flo.append(float('inf'))

  res = (None, None)
  shortest_len = float('inf')
  for i in xrange(len(words)):
    if words[i] in key_to_index:
      key_idx = key_to_index[words[i]]
      if key_idx == 0:
        shortest_lens_flo[0] = 1
      elif shortest_lens_flo[key_idx - 1] != float('inf'):
        shortest_lens_flo[key_idx] = i - last_occurrence[key_idx - 1] + shortest_lens_flo[key_idx - 1]
      last_occurrence[key_idx] = i
      if key_idx == (len(keywords) - 1):
        if shortest_lens_flo[key_idx] < shortest_len:
          shortest_len = shortest_lens_flo[key_idx]
          res = (i - shortest_len + 1, i)
  return res


def find_min_squential_cover(words, keywords):
  """
    From the problem's spec, now keywords are all distinct.
    The time complexity is roughly O(n)...
    The additional space complexity is O(m) where m is the number of keywords.
  """
  kw_map = {}
  start_kw_map = {}
  end_kw_map = {}
  for i in xrange(len(keywords)):
    if keywords[i] not in kw_map:
      kw_map[keywords[i]] = i
      start_kw_map[keywords[i]] = 0
      end_kw_map[keywords[i]] = 0

  res = (None, None)
  left = 0
  right = 0
  i = 0
  target_idx = 0
  need_reverse = False
  while i < len(words):
    if words[i] in kw_map:
      if kw_map[words[i]] == target_idx:
        start_kw_map[words[i]] = i
        end_kw_map[words[i]] = i
        if len(keywords) == 1:
          res = (i, i)
          break
        if target_idx == 0:
          left = i
        if target_idx < (len(keywords) - 1):
          target_idx += 1
        else:
          target_idx = 0
          right = i
          end_kw_map[words[i]] = i
          need_reverse = True
      else:
        end_kw_map[words[i]] = i
    if need_reverse:
      rev_target_start = len(keywords) - 2
      for j in xrange(rev_target_start, -1, -1):
        if j == rev_target_start:
          left = end_kw_map[keywords[j]]
        else:
          for k in xrange(left, start_kw_map[keywords[j]] - 1, -1):
            if words[k] == keywords[j]:
              left = k
              break
      if (res[0] == None and res[1] == None) or ((right - left) < (res[1] - res[0])):
        res = (left, right)
      if left != end_kw_map[keywords[0]]:
        i = end_kw_map[keywords[0]] - 1 # later i woulc be increment 1 in line 57
      need_reverse = False
    i += 1
  return res

def get_input(case=0):
  paragraph = 'My paramount object in this struggle is to save the Union and is not either to save or to destroy slavery If I could save the Union without freeing any slave I would do it and if I could save it by freeing all the slaves I would do it and if I could save it by freeing some and leaving others alone I would also do that'
  keywords = ['Union', 'save']
  ans = (10, 16)
  if case == 0:
    pass
  elif case == 1:
    paragraph = 'save ' + paragraph[:58] + 'save ' + paragraph[58:] + ' Union'
    ans = (11, 12)
  elif case == 2:
    paragraph = 'apple banana apple apple dog cat apple dog banana apple cat dog'
    keywords = ['banana', 'cat']
    ans = (8, 10)
  elif case == 3:
    paragraph = 'apple banana cat apple'
    keywords = ['banana', 'apple']
    ans = (1, 3)
  elif case == 4:
    paragraph = 'apple banana cat apple cat'
    keywords = ['cat']
    ans = (2,2)
  elif case == 5:
    paragraph = 'x c b x b a x a c a b x x a c b c x a a a x b b x a a c c'
    keywords = ['a', 'b', 'c']
    ans = (13, 16)
  return paragraph.split(' '), keywords, ans

def main():
  for case in xrange(6):
    print('--- case {} ---'.format(case))
    words, keywords, ans = get_input(case)
    print('Input:')
    print('words =', words)
    res = find_min_squential_cover_epi(words, keywords)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()


