from __future__ import print_function
from collections import deque

class Queue(object):
  def __init__(self):
    self.data = deque()
    self.max_history = deque()

  def enqueue(self, item):
    """
      The amortized time complexity is O(1) (that is the time complexity of n enqueues and dequeues is O(n))
      since an element can be added and removed from the self.max_history no more than once.
    """
    self.data.append(item)
    while self.max_history and self.max_history[-1][0]< item:
      self.max_history.pop()
    if (not self.max_history) or self.max_history[-1][0] > item:
      self.max_history.append([item, 1])
    elif self.max_history[-1][0] == item:
      self.max_history[-1][1] += 1

  def dequeue(self):
    """
      The time complexity is O(1)
    """
    if not self.data:
      raise ValueError('This queue is empty and dequeue failed.')
    res = self.data.popleft()
    if self.max_history[0][0] == res:
      self.max_history[0][1] -= 1
      if self.max_history[0][1] == 0:
        self.max_history.popleft()
    return res

  def get_max(self):
    """
      The time complexity is O(1)
    """
    return self.max_history[0][0]

def main():
  q = Queue()
  q.enqueue(10)
  q.enqueue(20)
  q.enqueue(30)
  q.enqueue(50)
  q.enqueue(40)
  q.enqueue(40)
  q.enqueue(40)
  q.enqueue(25)
  q.enqueue(30)

  print('data =', q.data)
  print('max_history =', q.max_history)
  print('get_max =', q.get_max())

  q.dequeue()
  q.dequeue()
  q.dequeue()
  q.dequeue()
  print('data =', q.data)
  print('max_history =', q.max_history)
  print('get_max =', q.get_max())

  q.dequeue()
  print('data =', q.data)
  print('max_history =', q.max_history)
  print('get_max =', q.get_max())


  q.enqueue(70)
  print('data =', q.data)
  print('max_history =', q.max_history)
  print('get_max =', q.get_max())

if __name__ == '__main__':
  main()
