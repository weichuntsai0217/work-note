"""
  Use python 3.6.8
"""
import threading

class Monitor(threading.Condition):
  odd_turn = True
  even_turn = False

  def __init__(self):
    threading.Condition.__init__(self)
    self.turn = Monitor.odd_turn

  def wait_run(self, target_turn):
    with self:
      while target_turn != self.turn:
        self.wait()

  def toggle_turn(self):
    with self:
      self.turn ^= True
      self.notify()


class PrintOdds(threading.Thread):
  def __init__(self, monitor):
    threading.Thread.__init__(self)
    self.monitor = monitor

  def run(self):
    for i in range(1, 100, 2):
      self.monitor.wait_run(Monitor.odd_turn)
      print(i)
      self.monitor.toggle_turn()

class PrintEvens(threading.Thread):
  def __init__(self, monitor):
    threading.Thread.__init__(self)
    self.monitor = monitor

  def run(self):
    for i in range(2, 101, 2):
      self.monitor.wait_run(Monitor.even_turn)
      print(i)
      self.monitor.toggle_turn()

def main():
  monitor = Monitor()
  odd = PrintOdds(monitor)
  even = PrintEvens(monitor)

  odd.start()
  even.start()

  odd.join()
  even.join()

if __name__ == '__main__':
  main()
