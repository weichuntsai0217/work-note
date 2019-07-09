from __future__ import print_function

class CircularQueue(object):
  factor = 2
  def __init__(self, max_len=1):
    self.data = [None] * max_len # mimic allocation behavior like C/C++
    self.size = 0
    self.head = 0
    self.tail = 0 # tail is to the index for writing data

  def enqueue(self, item):
    """
      The amortized time complexity is O(1)
    """
    if self.size == len(self.data):
      new_data = [None] * (self.size * CircularQueue.factor) # mimic allocation behavior like C/C++
      read_idx = self.head
      for i in xrange(self.size):
        new_data[i] = self.data[read_idx % self.size]
        read_idx += 1
      self.data = new_data
      self.head = 0
      self.tail = self.size
    self.data[self.tail] = item
    self.tail = (self.tail + 1) % len(self.data)
    self.size += 1

  def dequeue(self):
    """
      The time complexity is O(1)
    """
    if self.size:
      res = self.data[self.head]
      self.size -= 1
      self.head = (self.head + 1) % len(self.data)
      return res
    raise ValueError('This queue is empty and dequeue failed.')

  def get_size(self):
    return self.size

def main():
    cq = CircularQueue(4)
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())
    cq.enqueue(60)
    cq.enqueue(70)
    cq.enqueue(80)
    cq.enqueue(90)
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())
    print(cq.dequeue())
    print('--- Summary ---')
    print('head =', cq.head)
    print('tail =', cq.tail)
    print('size =', cq.size)
    print('data =', cq.data)

    print(cq.dequeue())
    print('--- Summary ---')
    print('head =', cq.head)
    print('tail =', cq.tail)
    print('size =', cq.size)
    print('data =', cq.data)

    cq.enqueue(100)
    print('--- Summary ---')
    print('head =', cq.head)
    print('tail =', cq.tail)
    print('size =', cq.size)
    print('data =', cq.data)

if __name__ == '__main__':
  main()
