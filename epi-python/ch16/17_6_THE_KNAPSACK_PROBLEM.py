from __future__ import print_function

def get_max_value(items, max_weight):
  """
    Time complexity: O(mn), m is the number of items and n is max_weight
  """
  table = []
  for i in xrange(len(items)):
    table.append([0] * (max_weight+1))

  for row, target in enumerate(items):
    for tmp_max_weight in xrange(max_weight+1):
      prev_row = row - 1 if (row - 1) >= 0 else row
      best_without_target = table[prev_row][tmp_max_weight]
      if target['w'] > tmp_max_weight:
        table[row][tmp_max_weight] = best_without_target
      else:
        with_target = table[prev_row][tmp_max_weight - target['w']] + target['v'] if prev_row != row else target['v']
        table[row][tmp_max_weight] = max(best_without_target, with_target)

  # show_table(table)
  return table[-1][-1]
    
def show_table(table):
  for row in table:
    print(row)

def get_input(hard=False):
  if hard:
    items = [
      {'id': 'A', 'v': 65, 'w': 20}, # 'v' is value and 'w' is weight
      {'id': 'B', 'v': 35, 'w': 8}, 
      {'id': 'C', 'v': 245, 'w': 60}, 
      {'id': 'D', 'v': 195, 'w': 55}, 
      {'id': 'E', 'v': 65, 'w': 40}, 
      {'id': 'F', 'v': 150, 'w': 70}, 
      {'id': 'G', 'v': 275, 'w': 85}, 
      {'id': 'H', 'v': 155, 'w': 25}, 
      {'id': 'I', 'v': 120, 'w': 30}, 
      {'id': 'J', 'v': 320, 'w': 65}, 
      {'id': 'K', 'v': 75, 'w': 75}, 
      {'id': 'L', 'v': 40, 'w': 10}, 
      {'id': 'M', 'v': 200, 'w': 95}, 
      {'id': 'N', 'v': 100, 'w': 50}, 
      {'id': 'O', 'v': 220, 'w': 40}, 
      {'id': 'P', 'v': 99, 'w': 10}, 
    ]
    max_weight = 130
    ans = 155 + 320 + 220
    return items, max_weight, ans
  else:
    items = [
      {'id': 'A', 'v': 60, 'w': 5}, # 'v' is value and 'w' is weight
      {'id': 'B', 'v': 50, 'w': 3}, 
      {'id': 'C', 'v': 70, 'w': 4}, 
      {'id': 'D', 'v': 30, 'w': 2}, 
    ]
    max_weight = 5
    ans = 50 + 30
    return items, max_weight, ans

def main():
  for arg in [False, True]:
    items, max_weight, ans = get_input(arg)
    print('Test success' if get_max_value(items, max_weight) == ans else 'Test failure')


if __name__ == '__main__':
  main()
