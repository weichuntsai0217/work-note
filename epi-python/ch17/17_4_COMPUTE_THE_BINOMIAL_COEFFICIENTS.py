from __future__ import print_function

def get_comb(n, k):
  """
    Time complexity: O(nk)
    Space complexity: O(nk)
    C^n_k = C^n-1_k + C^n-1_k-1
    Note that by definition, for n >= 0, C^n_0 = C^n_n = 1 (C^0_0 is also 1)
  """
  table = [] # table[a][b] means C^a_b
  for i in xrange(n+1):
    table.append([])
    for j in xrange(k+1):
      if i < j:
        table[i].append(0)
      elif i == j or j == 0:
        table[i].append(1)
      else:
        table[i].append(-1) # -1 means value unknown.
  return comb(n, k, table)


def comb(n, k, table):
  if table[n][k] != -1: return table[n][k]
  with_k = comb(n-1, k-1, table)
  without_k = comb(n-1, k, table)
  table[n][k] = with_k + without_k
  return table[n][k]

def show_table(table):
  for row in table:
    print(row)

def main():
  print(get_comb(0, 0))
  print(get_comb(0, 0) == 1)
  print(get_comb(5, 2))
  print(get_comb(5, 2) == 10)
  print(get_comb(10, 6))
  print(get_comb(10, 6) == 210)
  print(get_comb(52, 5))
  print(get_comb(52, 5) == 2598960)

if __name__ == '__main__':
  main()
