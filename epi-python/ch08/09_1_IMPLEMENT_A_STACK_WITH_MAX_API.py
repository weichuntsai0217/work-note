from __future__ import print_function

class Stack(object):
  """
    The time complexity is O(1) for get_max
    The additional space complexity for worst case is O(n) where n is the length of the stack data
    The additional space complexity for best case is O(1)
  """
  def __init__(self):
    self.data = []
    self.max_history = []
    # self.max_history = [[3,2], [4,1]], where [3, 2] means max val is 3 and counts are 2

  def peek(self):
    if self.data:
      return self.data[-1]
    return None

  def push(self, item):
    self.data.append(item)
    if self.max_history:
      if item == self.max_history[-1][0]:
        self.max_history[-1][1] += 1
      elif item > self.max_history[-1][0]:
        self.max_history.append([item, 1])
    else:
      self.max_history.append([item, 1])

  def pop(self):
    if not self.data:
      return None
    item = self.data.pop()
    if item == self.max_history[-1][0]:
      self.max_history[-1][1] -= 1
      if self.max_history[-1][1] == 0:
        self.max_history.pop()
    return item

  def get_max(self):
    if not self.max_history: return None
    return self.max_history[-1][0]

def get_input(case=0):
  if case == 0:
    ans_data = [2,2,1,4,5,5,3]
    ans_max_history = [[2,2], [4,1], [5,2]]
    ans_pop = [
      [3, 5, [5, 2]],
      [5, 5, [5, 1]],
      [5, 4, [4, 1]],
      [4, 2, [2, 2]],
      [1, 2, [2, 2]],
      [2, 2, [2, 1]],
      [2, None, None],
    ]
    return ans_data, ans_max_history, ans_pop

def main():
  for case in xrange(1):
    print('--- case {} ---'.format(case))
    ans_data, ans_max_history, ans_pop = get_input(case)
    print('Input:')
    print('ans_data =', ans_data)
    print('ans_max_history =', ans_max_history)
    print('ans_pop =', ans_pop)
    s = Stack()
    for item in ans_data:
      s.push(item)
    print('Ouput:')
    print('stack data =', s.data)
    print('stack max_history =', s.max_history)
    print('Test stack data success' if s.data == ans_data else 'Test stack data failure')
    print('Test stack max_history success' if s.max_history == ans_max_history else 'Test stack max_history failure')
    for idx, [pop_item, max_val, max_item] in enumerate(ans_pop):
      res_pop_item = s.pop()
      res_max_val = s.get_max()
      res_max_item = s.max_history[-1] if s.max_history else None
      if res_pop_item == pop_item and res_max_val == max_val and res_max_item == max_item:
        print('Test stack pop success for the last {} item'.format(idx))
      else:
        print('Test stack pop failure for the last {} item'.format(idx))

if __name__ == '__main__':
  main()
