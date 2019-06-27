from __future__ import print_function

def can_take_photo(teams):
  """
    We assume that the front row height <= the back row height is valid
  """
  team_a = teams[0]
  team_b = teams[1]
  if len(team_a) != len(team_b): return False
  length = len(team_a)
  last_index = length - 1
  team_a = sorted(team_a) # O(N * logN)
  team_b = sorted(team_b)
  if team_a[0] < team_b[0] and team_a[last_index] > team_b[last_index]:
    return False
  if team_b[0] < team_a[0] and team_b[last_index] > team_a[last_index]:
    return False
  team_front = team_a if team_a[0] < team_b[0] else team_b
  team_back = team_b if team_a[last_index] < team_b[last_index] else team_a
  for i in xrange(length):
    if team_front[i] > team_back[i]: return False
  return True
  
def get_input(not_valid=False, hard=False):
  def get_rdm(x):
    import random
    return sorted(x, key=lambda k: random.random())
  if not_valid:
    if hard:
      return (
        get_rdm([2, 4, 6, 8, 10, 10, 14, 16, 18, 20]),
        get_rdm([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),
      )
    return (
      get_rdm([2, 4, 4, 8]),
      get_rdm([1, 3, 5, 7]),
    )
  else:
    if hard:
      return (
        get_rdm([2, 4, 6, 8, 10, 11, 14, 16, 18, 20]),
        get_rdm([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]),
      )
    return (
      get_rdm([2, 4, 6, 8]),
      get_rdm([1, 3, 5, 7]),
    )

def main():
  print(can_take_photo(get_input()) == True)
  print(can_take_photo(get_input(False, True)) == True)
  print(can_take_photo(get_input(True)) == False)
  print(can_take_photo(get_input(True, True)) == False)

if __name__ == '__main__':
  main()
