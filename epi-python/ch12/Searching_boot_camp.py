from __future__ import print_function

class Student(object):
  def __init__(self, name=None, gpa=None):
    self.name = name
    self.gpa = gpa

  def __lt__(self, other):
    if self.gpa != other.gpa:
      return self.gpa > other.gpa # our GPA in the student list is in descending order.
    return self.name < other.name # python built-in str can compare each other in alphabet order.

  def __eq__(self, other):
    return (self.gpa == other.gpa) and (self.name == other.name)

  def __le__(self, other):
    return (self < other) or (self == other)

  def __ne__(self, other):
    return not (self == other)

  def __ge__(self, other):
    return not (self < other)

  def __gt__(self, other):
    return not (self <= other)

def bsearch(array, t):
  """
    The time complexity is O(logn) where n is the array length.
  """
  from bisect import bisect_left
  i = bisect_left(array, t)
  if (i != len(array)) and (t == array[i]):
    return i
  return -1

def is_in_student_list(array, t):
  return bsearch(array, t) >= 0


def get_input(case=0):
  array = [ Student(chr(ord('a') + 10 - i), i) for i in range(10, 0, -1)]
  array.append(Student('l', 1))
  if case == 0:
    t = Student('a', 11)
    ans = False
  elif case == 1:
    t = Student('l', 0)
    ans = False
  elif case == 2:
    t = Student('a', 10)
    ans = True
  elif case == 3:
    t = Student('l', 1)
    ans = True
  elif case == 4:
    t = Student('e', 6)
    ans = True
  elif case == 5:
    t = Student('e', 5.5)
    ans = False
  return array, t, ans

def show_students(sts):
  if isinstance(sts, list):
    for idx, st in enumerate(sts):
      print('idx = {} | name = {} | gpa = {}'.format(idx, st.name, st.gpa))
  else:
    print('name = {} | gpa = {}'.format(sts.name, sts.gpa))

def main():
  for case in xrange(6):
    print('--- case {} ---'.format(case))
    print('Input:')
    array, t, ans = get_input(case)
    show_students(t)
    res = is_in_student_list(array, t)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')


if __name__ == '__main__':
  main()
