"""
  Use python 3.6.8
"""
import threading

"""
  Please refer to EPI in python page 316 for this problem's solution.
  It explains clearly.
  Here I just practice to implement another python version of this problem.
"""

class Counter(object):
  count = 0

class Increment(threading.Thread):
  def __init__(self, counter, N):
    threading.Thread.__init__(self)
    self.counter = counter
    self.N = N

  def run(self):
    for i in range(self.N):
      self.counter.count += 1

def main():
  N = 10000
  threads = []
  for i in range(2):
    threads.append(Increment(Counter, N))
    threads[i].start()

  for i in range(2):
    threads[i].join()

  print('Counter.count =', Counter.count)

if __name__ == '__main__':
  main()
