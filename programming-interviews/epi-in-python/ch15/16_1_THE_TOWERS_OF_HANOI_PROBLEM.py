from __future__ import print_function

def hanoi(n):
  """
    The time complexity is O(2^n) (neglect show_pegs).
    The additional space complexity is O(n).
  """
  pegs = [
   range(n, 0, -1),
   [],
   [],
  ]
  show_pegs(pegs)
  def transfer(num_rigns_to_move, pegs, from_idx, to_idx, use_idx):
    if num_rigns_to_move > 0:
      transfer(num_rigns_to_move - 1, pegs, from_idx, use_idx, to_idx)
      pegs[to_idx].append(pegs[from_idx].pop())
      show_pegs(pegs)
      transfer(num_rigns_to_move - 1, pegs, use_idx, to_idx, from_idx)
  transfer(n, pegs, 0, 1, 2)

  return pegs

def show_pegs(pegs):
  print('peg status:')
  for p in pegs:
    print(p)

def get_input(case=0):
  if case == 0:
    return 3
  elif case == 1:
    return 4

def main():
  for case in xrange(2):
    print('--- case {} ---'.format(case))
    print('Input:')
    n = get_input(case)
    print('Output:')
    pegs = hanoi(n)
    print('Final:')
    show_pegs(pegs)

if __name__ == '__main__':
  main()
