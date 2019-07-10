from __future__ import print_function

class QueueByStack(object):
  def __init__(self):
    self.enq = []
    self.deq = []

  def enqueue(self, item):
    """
      The time complexity is O(1)
    """
    self.enq.append(item)

  def dequeue(self):
		""" 
			The amortized time complexity is O(1).
			Why O(1) ? Let's assume the queue is empty at first, then you push k items in the queue (push k times)
			then you want to pop k items. But now `self.deq` is empty so you have to pop `self.enq` k times and push
			these k items into `self.deq`, and finally you have to pop k times from `self.deq`. In the above process,
			you do 4*k times operation on k items, so each item take 4k/k = 4 times operation, that is O(4) = O(1)
		"""
    if not self.deq:
      while self.enq:
        self.deq.append(self.enq.pop())
    if self.deq:
      return self.deq.pop()
    else:
      raise ValueError('This queue is empty and dequeue failed.')

def main():
  qbs = QueueByStack()
  qbs.enqueue(1)
  qbs.enqueue(2)
  qbs.enqueue(3)
  qbs.enqueue(4)
  print('Before dequeue:')
  print('enq =', qbs.enq)
  print('deq =', qbs.deq)

  ele = qbs.dequeue()

  print('After 1 dequeue:')
  print('The dequeued element =', ele)
  print('enq =', qbs.enq)
  print('deq =', qbs.deq)

  eles = []
  eles.append(qbs.dequeue())
  eles.append(qbs.dequeue())
  eles.append(qbs.dequeue())

  print('After 3 dequeue:')
  print('The dequeued elements =', eles)
  print('enq =', qbs.enq)
  print('deq =', qbs.deq)

if __name__ == '__main__':
  main()
