from __future__ import print_function
import threading

"""
  Please refer to EPI page 378 for this problem's solution.
  It explains clearly.
  Here I just practice to implement the python version of this problem.
"""

class Counter(object):
  count = 0

class Increment(threading.Thread):
  def __init__(self, counter, N):
    threading.Thread.__init__(self)
    self.counter = counter
    self.N = N

  def run(self):
    for i in xrange(self.N):
      self.counter.count += 1

def main():
  N = 10000
  threads = []
  for i in xrange(2):
    threads.append(Increment(Counter, N))
    threads[i].start()

  for i in xrange(2):
    threads[i].join()

  print('Counter.count =', Counter.count)

if __name__ == '__main__':
  main()
