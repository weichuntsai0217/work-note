# not solved for n_max >= 100000000 ...
from datetime import datetime
from math import pow
skip = [
  pow(10, 1),
  pow(10, 2),
  pow(10, 3),
  pow(10, 4),
  pow(10, 5),
  pow(10, 6),
  pow(10, 7),
  pow(10, 8),
  pow(10, 9),
  pow(10, 10),
  pow(10, 11),
  pow(10, 12),
]
res = long(1)
i = long(1)
# n_max = long(1000000000000)
n_max = long(10000000)
print datetime.now()

while i <= n_max:
  res *= i
  while res % 10 == 0:
    res /= 10
  tmp = str(res)
  l = len(tmp)
  if l > 7:
    tmp = tmp[l - 7:]
    res = long(tmp)
  i += 1
  
print res
print datetime.now()
'''
# for i in range(1, 1000000000001):
for i in xrange(10000001,  1000000000001):
  if i not in skip:
    res *= i
  while res % 10 == 0:
    res /= 10
  tmp = str(res)
  l = len(tmp)
  if l > 7:
    tmp = tmp[l - 7:]
    res = long(tmp)
print res
'''
