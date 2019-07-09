"""
  Use python 3.6.8
"""
import threading
import time

class Semaphore(object):
  def __init__(self, max_available):
    self.cv = threading.Condition()
    self.max_available = max_available
    self.taken = 0

  def acquire(self):
    print('before: self.taken =', self.taken)
    self.cv.acquire()
    while self.taken == self.max_available:
      print('middle: self.taken =', self.taken)
      self.cv.wait()
    self.taken += 1
    print('after: self.taken =', self.taken)
    self.cv.release()

  def release(self):
    self.cv.acquire()
    self.taken -= 1
    self.cv.notify()
    self.cv.release()

class Runner(threading.Thread):
  def __init__(self, name, semaphore):
    threading.Thread.__init__(self)
    self.name = name
    self.semaphore = semaphore

  def run(self):
    while True:
      self.semaphore.acquire()
      print('I am', self.name)
      time.sleep(1)
      self.semaphore.release()

def main():
  sm = Semaphore(2)
  ts = [Runner('t' + str(i), sm) for i in range(1, 5)]
  for thread in ts:
    thread.start()
  for thread in ts:
    thread.join()

if __name__ == '__main__':
  main()
