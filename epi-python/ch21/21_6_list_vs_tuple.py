"""
  Use python 3.6.8
"""
"""
  # Question: In what ways are lists and tuples similar, and in what ways are they different?

  ## The similar parts
  1. They both represent a sequence of elements.
  2. They both use the same syntax to access the i-th element of the sequence.
  3. They both support the `in` operator for memebership checking.

  ## The different pars
  1. lists are mutable and tuples are immutable. This means that you can not change the element at
     index i or add/delete from a tuple.
  2. tuples are slightly faster to build and access, and have a smaller memory footprint.
  3. tuples can be put in sets, and used as map keys in dict, but lists cannot because lists don't implement
     hash method.

  ## Other notes
  If an object implements its hash method, it can be put in sets. However if this object is also mutable
  and, after this object is changed, the lookup for this object in the set would fail.
  So basically, immutable objects are more container-friendly and thread-safe.
  Please see the following code example.
"""

class A(object):
  def __init__(self, x):
    self.x = x

  def __eq__(self, other):
    return isinstance(other, A) and (self.x == other.x)

  def __hash__(self):
    return self.x * 113 + 113

def main():
  u = A(42)
  v = A(42)
  U = (u,)
  V = (v,)
  S = set([U])
  print(u == v) # True
  print(U in S) # True
  print(V in S) # True
  u.x = 28
  print(u == v) # False
  print(U in S) # False, because the calculated bucket now is different.
  print(V in S) # False, because x attribute now is different, even finding the same bucket still doesn't work.


if __name__ == '__main__':
  main()
