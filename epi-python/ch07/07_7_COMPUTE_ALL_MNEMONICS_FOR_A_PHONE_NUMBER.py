from __future__ import print_function

def recursive(s, table, i, prefix, res):
  if i < len(s):
    prefixes = list(table[s[i]])
    for p in prefixes:
      recursive(s, table, i+1, prefix+p, res)
  else:
    res.append(prefix)



def get_mnemonics_for_a_phone_number(s):
  """
    The time complexity O(n*4^n) where n is the length of s
  """
  table = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
  }
  res = []

  if not s: return None
  if len(s) == 1: return list(table[s])
  
  recursive(s, table, 0, '', res)
  return res

def get_input(case=0):
  if case == 0:
    return '2', list('ABC')
  elif case == 1:
    return '23', sorted(['AD', 'AE', 'AF', 'BD', 'BE', 'BF', 'CD', 'CE', 'CF'])
  elif case == 2:
    return '22', sorted(['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC'])
  elif case == 3:
    return '567', sorted([
      'JMP', 'JMQ', 'JMR', 'JMS', 'JNP', 'JNQ', 'JNR', 'JNS', 'JOP', 'JOQ', 'JOR', 'JOS',
      'KMP', 'KMQ', 'KMR', 'KMS', 'KNP', 'KNQ', 'KNR', 'KNS', 'KOP', 'KOQ', 'KOR', 'KOS',
      'LMP', 'LMQ', 'LMR', 'LMS', 'LNP', 'LNQ', 'LNR', 'LNS', 'LOP', 'LOQ', 'LOR', 'LOS',
    ])


def main():
  for case in xrange(4):
    s, ans = get_input(case)
    res = sorted(get_mnemonics_for_a_phone_number(s))
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
