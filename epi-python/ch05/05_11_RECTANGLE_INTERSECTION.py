from __future__ import print_function

def is_intersec(a, b):
  chk_x = ((a['x'] + a['w']) > b['x']) and ((b['x'] + b['w']) > a['x'] )
  chk_y = ((a['y'] + a['h']) > b['y']) and ((b['y'] + b['h']) > a['y'] )
  return chk_x and chk_y

def rec_intersec(a, b):
  """
    Every rectangle is represented as a dict, each dict has 4 keys:
    The key 'x' represents the x coordinate of the bottom-left vertex.
    The key 'y' represents the y coordinate of the bottom-left vertex.
    The key 'w' represents the width.
    The key 'h' represents the height.
    Ex:
      a = {
        'x': 0,
        'y': 1,
        'w': 2,
        'h': 3,
      }
      b = {
        'x': 4,
        'y': 5,
        'w': 2,
        'h': 3,
      }
    Time complexity is O(1).
  """
  if is_intersec(a, b):
    x = max(a['x'], b['x'])
    y = max(a['y'], b['y'])
    w = min(a['x'] + a['w'], b['x'] + b['w']) - x
    h = min(a['y'] + a['h'], b['y'] + b['h']) - y
    return { 'x': x, 'y': y, 'w': w, 'h': h }
  else:
    return None #

def get_input(case=0):
  if case == 0:
    a = {
      'x': 0,
      'y': 1,
      'w': 2,
      'h': 3,
    }
    b = {
      'x': 4,
      'y': 5,
      'w': 2,
      'h': 3,
    }
    inter = None
    return a, b, inter
  elif case == 1:
    a = {
      'x': 0,
      'y': 1,
      'w': 2,
      'h': 3,
    }
    b = {
      'x': 1,
      'y': 3,
      'w': 2,
      'h': 3,
    }
    inter = {
      'x': 1,
      'y': 3,
      'w': 1,
      'h': 1,
    }
    return a, b, inter
  elif case == 2:
    a = {
      'x': 0,
      'y': 1,
      'w': 2,
      'h': 3,
    }
    b = {
      'x': 1,
      'y': 1,
      'w': 2,
      'h': 3,
    }
    inter = {
      'x': 1,
      'y': 1,
      'w': 1,
      'h': 3,
    }
    return a, b, inter
  elif case == 3:
    a = {
      'x': 0,
      'y': 1,
      'w': 2,
      'h': 3,
    }
    b = {
      'x': 1,
      'y': -1,
      'w': 2,
      'h': 3,
    }
    inter = {
      'x': 1,
      'y': 1,
      'w': 1,
      'h': 1,
    }
    return a, b, inter
  elif case == 4:
    a = {
      'x': 0,
      'y': 1,
      'w': 2,
      'h': 3,
    }
    b = {
      'x': 0,
      'y': -1,
      'w': 2,
      'h': 3,
    }
    inter = {
      'x': 0,
      'y': 1,
      'w': 2,
      'h': 1,
    }
    return a, b, inter
  elif case == 5:
    a = {
      'x': 0,
      'y': 1,
      'w': 2,
      'h': 3,
    }
    b = {
      'x': -1,
      'y': 2,
      'w': 4,
      'h': 1,
    }
    inter = {
      'x': 0,
      'y': 2,
      'w': 2,
      'h': 1,
    }
    return a, b, inter
  elif case == 6:
    a = {
      'x': 0,
      'y': 1,
      'w': 2,
      'h': 3,
    }
    b = {
      'x': 0,
      'y': 2,
      'w': 1,
      'h': 1,
    }
    inter = {
      'x': 0,
      'y': 2,
      'w': 1,
      'h': 1,
    }
    return a, b, inter

def main():
  for i in xrange(7):
    a, b, ans = get_input(i)
    res = rec_intersec(a, b)
    print(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
