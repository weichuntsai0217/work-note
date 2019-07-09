"""
  Use python 3.6.8
"""
import threading
import time
import random

class Account(object):

  _global_id = 0

  def __init__(self, balance):
    self._balance = balance
    self._id = Account._global_id
    Account._global_id += 1
    self._lock = threading.RLock()

  def get_balance(self):
    return self._balance

  @staticmethod
  def transfer(acc_from, acc_to, amount):
    th = threading.Thread(target=acc_from._move, args=(acc_to, amount))
    th.start()

  def _move(self, acc_to, amount):
    with self._lock:
      if amount > self._balance:
        return False
      acc_to._balance += amount
      self._balance -= amount
      print('acount {}: {}'.format(self._id, self._balance))
      return True


def main():
  acc_1 = Account(100)
  acc_2 = Account(200)
  while True:
    Account.transfer(acc_1, acc_2, 1)
    Account.transfer(acc_2, acc_1, 2)


if __name__ == '__main__':
  main()
