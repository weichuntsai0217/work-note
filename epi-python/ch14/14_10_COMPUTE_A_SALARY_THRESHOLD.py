from __future__ import print_function

def get_salary_threshold(salaries, target):
  """
    The time complexity is O(n * logn) where n is the length of salaries.
    The additional space complexity is O(1).
  """
  salaries.sort()
  first_unadjusted_sum = 0
  for i in xrange(len(salaries)):
    last_adjusted_sum = salaries[i] * (len(salaries) - i)
    if (first_unadjusted_sum + last_adjusted_sum) >= target:
      return (target - first_unadjusted_sum) / (len(salaries) - i)
    first_unadjusted_sum += salaries[i]
  return -1 # the sum of salaries is less than target

def get_input(case=0):
  last_salaries = [90., 30., 100., 40., 20.]
  target = 210.
  ans = 60.
  if case == 0:
    pass
  elif case == 1:
    target = 270.
    ans = 90.
  elif case == 2:
    target = 155.
    ans = 35.
  return last_salaries, target, ans

def main():
  for case in xrange(3):
    print('--- case {} ---'.format(case))
    last_salaries, target, ans = get_input(case)
    print('Input:')
    print('last_salaries =', last_salaries)
    print('target =', target)
    res = get_salary_threshold(last_salaries, target)
    print('Output:')
    print('res =', res)
    print('ans =', ans)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()








