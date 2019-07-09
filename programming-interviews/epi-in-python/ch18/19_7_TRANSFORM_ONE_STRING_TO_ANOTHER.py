from __future__ import print_function

class Node(object):
  def __init__(self, value, seq_len=-1):
    self.value = value
    self.seq_len = seq_len

def is_prod_seq(words, src, dst): # words is a list of strs
  show_input(words, src, dst)
  if len(src) != len(dst): return -1
  if src not in words or dst not in words: return -1 # src and dst in not in the dictionary
  if src == dst: return 1 # naive case
  mapping = {}
  for s in words:
    if len(s) == len(src) and s != src:
      mapping[s] = True
  src_node = Node(src, 1)
  queue = [src_node]
  while queue:
    # show_queue(queue)
    cur = queue.pop(0)
    value = cur.value
    for i in xrange(len(value)):
      if not mapping: break
      start = ''
      end = ''
      if i == 0:
        end = value[i+1:]
      elif i == len(value) - 1:
        start = value[0:i]
      else:
        start = value[0:i]
        end = value[i+1:]
      for j in xrange(97, 97+26):
        if not mapping: break
        rep = chr(j)
        tmp = start + rep + end
        if tmp in mapping:
          tmp_node = Node(tmp, cur.seq_len + 1)
          mapping.pop(tmp, None)
          queue.append(tmp_node)
          if tmp == dst:
            return tmp_node.seq_len
  return -1

def show_queue(q):
  res = []
  for n in q:
    res.append(n.value)
  print(' -> '.join(res))

def show_input(words, src, dst):
  print('words =', words)
  print('src =', src)
  print('dst =', dst)

def get_input(is_no_seq=False, level='medium'):
  if level == 'easy':
    src = 'cat'
    dst = 'zzz' if is_no_seq else 'cft'
    words = ['cbt', 'cct', dst, 'cdt', 'cet', src]
    return src, dst, words
  elif level == 'medium':
    src = 'cat'
    dst = 'zzz' if is_no_seq else 'dog'
    words = ['bat', 'cot', dst, 'dag', 'dot', src]
    return src, dst, words
  else:
    src = 'cat'
    dst = 'die' if is_no_seq else 'dog'
    words = ['bat', 'cot', dst, 'dag', 'dot', src, 'doc', 'too', 'cow']
    return src, dst, words

def main():
  """
    The worst case time complexity is O(d * n^2),
    where d is the number of total words and n is the length of src and dst.
  """
  src, dst, words = get_input(False, 'easy')
  print(is_prod_seq(words, src, dst), '\n')
  src, dst, words = get_input(False, 'medium')
  print(is_prod_seq(words, src, dst), '\n')
  src, dst, words = get_input(False, 'hard')
  print(is_prod_seq(words, src, dst), '\n')
  src, dst, words = get_input(True, 'easy')
  print(is_prod_seq(words, src, dst), '\n')
  src, dst, words = get_input(True, 'medium')
  print(is_prod_seq(words, src, dst), '\n')
  src, dst, words = get_input(True, 'hard')
  print(is_prod_seq(words, src, dst), '\n')

if __name__ == '__main__':
  main()
