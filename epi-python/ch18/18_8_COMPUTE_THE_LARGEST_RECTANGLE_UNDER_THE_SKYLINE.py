from __future__ import print_function

def get_max_area(blds):
  """
    Time complexity is O(n) where n is the length of blds
    Additional space complexity is O(n) where n is is the length of blds
  """
  if not blds: return 0
  stack = [
    [0, blds[0]]
  ]
  max_area = stack[0][1]
  for i in xrange(1, len(blds)):
    # print(stack)
    if stack[-1][1] < blds[i]:
      stack.append([i, blds[i]])
    else:
      max_area = check_area(stack, blds, i, max_area)
  if stack:
    max_area = pick_area(stack, len(blds)-1, max_area)
  return max_area

def pick_area(stack, end_idx, max_area):
  # print(end_idx, stack)
  while stack:
    item = stack.pop()
    tmp = (end_idx - item[0] + 1) * item[1]
    # print(tmp)
    if tmp > max_area: max_area = tmp
  return max_area
   

def check_area(stack, blds, end_idx, max_area):
  left_idx = end_idx
  while stack:
    if stack[-1][1] > blds[end_idx]:
      item = stack.pop()
      left_idx = item[0]
      tmp = (end_idx - item[0]) * item[1]
      # print(tmp, end_idx, item)
      if tmp > max_area:
        max_area = tmp
    elif stack[-1][1] < blds[end_idx]:
      stack.append([left_idx, blds[end_idx]])
      break
    else:
      break
  return max_area
 
def get_input(hard=False):
  if hard:
    return [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 5, 5, 2, 1, 3], 25
  return [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3], 20
  

def main():
  for arg in [False, True]:
    blds, ans = get_input(arg)
    res = get_max_area(blds)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
