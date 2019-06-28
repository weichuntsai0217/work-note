import time
import threading
import random

class Producer(threading.Thread):
  def __init__(self, integers, condition):
    threading.Thread.__init__(self)
    self.integers = integers
    self.condition = condition
    self.counter = 0

  def run(self):
    while True:
      self.condition.acquire()
      print('producer acquire')
      x = random.randint(1, 10)
      self.integers.append(x)
      print('producer append', x)
      print('producer says', self.integers)
      print('producer nofity')
      self.condition.notify() # notify would wake up the sleeing thread, but notify would not release the lock.
      print('producer release')
      self.condition.release()
      time.sleep(1)

class Consumer(threading.Thread):
  def __init__(self, integers, condition):
    threading.Thread.__init__(self)
    self.integers = integers
    self.condition = condition

  def run(self):
    while True:
      self.condition.acquire()
      print('consumer acquire')
      while True:
        if self.integers:
          x = self.integers.pop()
          print('consumer pop ', x)
          print('consumer says', self.integers)
          break
        print('consumer wait')
        self.condition.wait()
        """
        1. wait would release the lock and make the thread go to sleep.
        2. At some future time, when the thread is waken up by other thread triggering notify,
        3. After the thread is awakened, this thread would not return from wait and continues acquire the lock (still in the code block of wait), and if it gets the lock, then wait ends and then the thread return from wait.
        """
      print('consumer release')
      self.condition.release()

if __name__ == '__main__':
  integers = []
  condition = threading.Condition()
  prd = Producer(integers, condition)
  csm = Consumer(integers, condition)
  prd.start()
  csm.start()
  prd.join()
  csm.join()

