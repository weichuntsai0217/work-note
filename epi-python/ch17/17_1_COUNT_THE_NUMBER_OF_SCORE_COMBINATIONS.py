from __future__ import print_function

def count_combination_stupid(final_score, play_scores):
  play_scores = sorted(play_scores) # ascending sorting
  meta_data = []
  for ps in play_scores:
    meta_data.append({
      'ps': ps,
      'ub': (final_score / ps) + 1 # the upper factor bound for each play score
    })
  
  counts = iterate_count(final_score, meta_data, 0)
  return counts

def iterate_count(rs, meta_data, meta_index): # rs is residual score
  counts = 0
  if meta_index >= len(meta_data): return counts
  target = meta_data[meta_index]
  for i in xrange(target['ub']):
    # print(target['ps'])
    diff = rs - target['ps'] * i
    if diff == 0:
      counts += 1
    elif diff > 0:
      counts += iterate_count(diff, meta_data, meta_index + 1)
    else:
      return counts
  return counts

def count_combination_dp(final_score, play_scores):
  """
    Time complexity: O(sn), s is ths final score and n is the length of play_scores
    Space complexity: O(sn), s is ths final score and n is the length of play_scores
  """
  play_scores = sorted(play_scores) # ascending sorting
  table = []
  for i in xrange(len(play_scores)):
    table.append([])
  for tmp_s in xrange(final_score + 1):
    table[0].append(1 if (tmp_s % play_scores[0]) == 0 else 0)

  for row in xrange(1, len(play_scores)):
    for col in xrange(final_score + 1):
      prv_row = row - 1
      prv_col = col - play_scores[row]
      val = table[prv_row][col] + (table[row][prv_col] if prv_col >= 0 else 0)
      table[row].append(val)
  # show_table(table)
  return table[len(play_scores) - 1][final_score]

def show_table(table):
  for row in table:
    print(row)


def main():
  print('Use stupid method')
  print(count_combination_stupid(1, [2, 3, 7]) == 0)
  print(count_combination_stupid(6, [2, 3, 7]) == 2)
  print(count_combination_stupid(12, [2, 3, 7]) == 4)
  
  print('==============================')
  print('Use dynamic programming method')
  print(count_combination_dp(1, [2, 3, 7]) == 0)
  print(count_combination_dp(6, [2, 3, 7]) == 2)
  print(count_combination_dp(12, [2, 3, 7]) == 4)

if __name__ == '__main__':
  main()
