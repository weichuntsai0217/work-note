from __future__ import print_function
import heapq

class Stack(object):
  """
    The time complexity for pop and push are O(logn) where n is the number of elements in the current stack.
  """
  def __init__(self):
    self.min_heap = []
    self.idx = -1 # mimic timestamp

  def push(self, item):
    heapq.heappush(self.min_heap, (self.idx, item))
    self.idx -= 1 # more minus means more late to push
 
  def pop(self):
    x = heapq.heappop(self.min_heap)
    return x[1]

  def peek(self):
    return self.min_heap[0][1]
    

def main():
  st = Stack()
  st.push('a')
  st.push('b')
  st.push('c')
  st.push('d')
  print('After push 4 items, stack length =', len(st.min_heap))
  print(st.pop() == 'd')
  print(st.pop() == 'c')
  st.push('e')
  print(st.pop() == 'e')
  print(st.pop() == 'b')
  print(st.pop() == 'a')
  print('After all items are popped, stack length =', len(st.min_heap))
  print(st.idx == -6)

if __name__ == '__main__':
  main()
