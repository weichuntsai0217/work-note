from __future__ import print_function

def get_number_of_traverse_ways(rows, cols):
  """
    Time complexity: O(min(rows, cols) - 1)
    This problem can be solved analytically by using combination.
  """
  if rows < 1 or cols < 1: return 0 # this is an invalid 2D array
  n = rows + cols - 2
  m = (cols - 1) if cols > rows else (rows - 1)
  # the answer is n! / (m! * (n - m)!)
  nm = 1
  index = n
  while index > m: # do (n - m) multiplication
    nm *= index
    index -= 1

  dn = 1
  index = n - m
  while index > 0: # do (n - m) multiplication
    dn *= index
    index -= 1
  
  return nm / dn
    

def main():
  print(get_number_of_traverse_ways(5, 5) == 70)
  print(get_number_of_traverse_ways(6, 5) == 126)

if __name__ == '__main__':
  main()
