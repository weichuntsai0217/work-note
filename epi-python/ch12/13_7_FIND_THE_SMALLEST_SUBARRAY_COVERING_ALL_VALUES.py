from __future__ import print_function

def find_min_cover_epi(words, keywords):
  """
    This solution can handle duplicates in keywords, for example: 'aa', 'b' , 'aa', and in this case, your subarray
    should contains two 'aa's and one 'b'
    The time complexity is O(n) where n is the length of words.
    The additional space complexity is O(1)
  """
  kw_counts = {}
  for kw in keywords:
    if kw not in kw_counts:
      kw_counts[kw] = 0
    kw_counts[kw] += 1

  res = (None, None)
  left = 0
  right = 0
  remain_kw_counts = len(keywords)
  while right < len(words):
    if words[right] in kw_counts:
      kw_counts[words[right]] -= 1
      if kw_counts[words[right]] >= 0:
        remain_kw_counts -= 1
    
    while remain_kw_counts == 0:
      if (res[0] == None and res [1] == None) or ((right - left) < (res[1] - res[0])):
        res = (left, right)

      if words[left] in kw_counts:
        kw_counts[words[left]] += 1
        if kw_counts[words[left]] > 0:
          remain_kw_counts += 1
      left += 1

    right += 1
  return res

def find_min_cover(words, keywords):
  """
    This solution cannot handle duplicates in keywords and its time & space complexity is worse.
    The time complexity is O(n^2) where n is the length of words.
    The additional space complexity is O(n).
  """
  def set_mapping(mapping, key):
      mapping[key] = True

  w_freq = {}
  for kw in keywords:
    set_mapping(w_freq, kw)

  helper = []
  for i in xrange(len(words)): # pick keywords and their indices only.
    if words[i] in w_freq:
      helper.append((i, words[i]))
  
  res = (0, float('inf')) # the 1st item is start index, and the 2nd item is end index.
  for i in xrange(len(helper)):
    unseen_counts = len(keywords)
    unseen_map = {}
    for j in xrange(i, len(helper)):
      if helper[j][1] not in unseen_map:
        set_mapping(unseen_map, helper[j][1])
        unseen_counts -= 1
        if unseen_counts == 0:
          if (helper[j][0] - helper[i][0]) < res[1] - res[0]:
            res = (helper[i][0], helper[j][0])
          break
  return res


def get_input(case=0):
  paragraph = 'My paramount object in this struggle is to save the Union and is not either to save or to destroy slavery If I could save the Union without freeing any slave I would do it and if I could save it by freeing all the slaves I would do it and if I could save it by freeing some and leaving others alone I would also do that'
  keywords = ['Union', 'save']
  ans = (8, 10)
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
    paragraph = 'apple banana apple apple dog cat apple dog banana apple cat banana dog'
    keywords = ['banana', 'cat', 'banana']
    ans = (8, 11)
  return paragraph.split(' '), keywords, ans

def main():
  for case in xrange(4):
    print('--- case {} ---'.format(case))
    words, keywords, ans = get_input(case)
    print('Input:')
    print('words =', words)
    res = find_min_cover_epi(words, keywords)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()

