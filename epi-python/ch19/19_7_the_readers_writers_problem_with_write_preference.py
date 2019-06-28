"""
  Use python 3.6.8
"""
import threading
import time
import random

class ReaderWriter(object):
  LR = threading.Condition()  # reader lock
  LW = threading.Condition() # writer lock
  read_count = 0 # the number of readers
  data = 0

class Reader(threading.Thread):
  def run(self):
    while True:
      time.sleep(random.random()) # just for test
      with ReaderWriter.LW:
        pass
      with ReaderWriter.LR:
        ReaderWriter.read_count += 1
      print('Reading data {}.'.format(ReaderWriter.data))
      with ReaderWriter.LR:
        ReaderWriter.read_count -= 1
        ReaderWriter.LR.notify()
  
class Writer(threading.Thread):
  def run(self):
    while True:
      time.sleep(random.random()/2) # just for test
      with ReaderWriter.LW:
        done = False
        while not done:
          with ReaderWriter.LR:
            if ReaderWriter.read_count == 0:
              ReaderWriter.data += 1
              print('Writing data as {}'.format(ReaderWriter.data))
              done = True
            else:
              while ReaderWriter.read_count != 0:
                ReaderWriter.LR.wait()
                """
                  Why we need `while ReaderWriter.read_count != 0` ?
                  Ans:
                    Because we want to avoid busy waiting.
                    In ReaderWriter.LR.wait(), when the writer thread gets awakened (get notified by reader thread),
                    the writer thread would triy to get LR. After the writer thread gets LR,
                    there 2 situations (situation 1 is the key reason of `while ReaderWriter.read_count != 0`):
                      1. ReaderWriter.read_count is not 0:
                        In this case, we know that only reader threads can reduce ReaderWriter.read_count
                        and then can help writer threads to do line 34 ~ 36, and writer threads should not
                        compete LR with reader threads, so we use `while ReaderWriter.read_count != 0`
                        to make writer threads wait again (sleep until be notified).
                      2. ReaderWriter.read_count is 0:
                        In this case, we want the writer thread do line 34 ~ 36,
                        and `while ReaderWriter.read_count != 0` does nothing.
                """

def main():
  readers = [Reader() for i in range(4)]
  writers = [Writer() for i in range(2)]
  for r in readers:
    r.start()
  for w in writers:
    w.start()
  for r in readers:
    r.join()
  for w in writers:
    w.join()

if __name__ == '__main__':
  main()

