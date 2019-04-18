from __future__ import print_function

def multiply(x, y):
  """
    Note that m digits times n digits, the result is (m+n) digits or (m + n -1) digits
    Time complexity is O(mn) where m is the number of digits of x and n is the number of digits of y.
  """
  if x[0] * y[0] == 0: return [0]
  sign = -1 if (x[0] * y[0]) < 0 else 1
  x[0] = abs(x[0])
  y[0] = abs(y[0])
  product = [0] * (len(x) + len(y))
  for i in xrange(len(y) - 1, -1, -1):
    for j in xrange(len(x) - 1, -1, -1):
      tmp = product[i + j + 1] + y[i] * x[j]
      product[i + j + 1] = tmp % 10
      product[i + j] = product[i + j] + tmp / 10

  if product[0] == 0: product.pop(0)
  product[0] = product[0] * sign
  return product

def get_input(case=0):
  if case == 0:
    return [0], [7,3,4], [0]
  elif case == 1:
    return [1,0], [1,0,0], [1,0,0,0]
  elif case == 2:
    return [9,9], [9,9,9], [9,8,9,0,1]
  elif case == 3:
    return [1,2,3], [8, 9], [1, 0, 9, 4, 7]
  elif case == 4:
    x = [1, 9, 3, 7, 0, 7, 7, 2, 1]
    y = [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]
    ans = [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7]
    return x, y, ans



def main():
  for arg in xrange(5):
    x, y, ans = get_input(arg)
    res = multiply(x, y)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
