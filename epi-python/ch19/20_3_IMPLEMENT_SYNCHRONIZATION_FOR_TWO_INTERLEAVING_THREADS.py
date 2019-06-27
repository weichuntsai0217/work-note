from __future__ import print_function
import threading

cur_turn = 'odd'

class PrintOdds(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.src = iter(xrange(1, 101, 2))

  def run(self):
    global cur_turn
    while True:
      if cur_turn == 'odd':
        try:
          print(self.src.next())
          cur_turn = 'even'
        except StopIteration:
          cur_turn = 'even'
          break


class PrintEvens(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.src = iter(xrange(2, 101, 2))

  def run(self):
    global cur_turn
    while True:
      if cur_turn == 'even':
        try:
          print(self.src.next())
          cur_turn = 'odd'
        except StopIteration:
          cur_turn = 'odd'
          break


def main():
  odd = PrintOdds()
  even = PrintEvens()

  odd.start()
  even.start()

  odd.join()
  even.join()

if __name__ == '__main__':
  main()
