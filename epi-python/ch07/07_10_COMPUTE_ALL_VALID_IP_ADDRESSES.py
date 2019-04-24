from __future__ import print_function

def is_valid(s):
  if len(s) < 1: return False
  number = int(s)
  if (len(s) > 1) and (number == 0): return False # '00' or '000' or '00000' (more than 1 zeros) are not valid.
  if number <= 255: return True


def recursive(s, start, prefix, quota, res):
  if quota <= 0:
    last = s[start:len(s)]
    if is_valid(last):
      res.append(prefix+last)
    return

  for i in xrange(start, start+3):
    if i < len(s) and is_valid(s[start:i+1]):
      next_prefix = prefix + s[start:i+1] + '.'
      recursive(s, i+1, next_prefix, quota - 1, res)

def compute_all_valid_ip_address(s):
  """
    The time complexity is O(1)
    The total number of IP addresses is a constant (2^32), implying an O(1) time complexity for the above algorithm.
  """
  res = []
  recursive(s, 0, '', 3, res)
  return res

def get_input(case=0):
  if case == 0:
    ans = [
      '1.92.168.11',
      '19.2.168.11',
      '19.21.68.11',
      '19.216.8.11',
      '19.216.81.1',
      '192.1.68.11',
      '192.16.8.11',
      '192.16.81.1',
      '192.168.1.1',
    ]
    return '19216811', ans
  elif case == 1:
    return '19216000', ['192.160.0.0']
  elif case == 2:
    return '000', []
  elif case == 3:
    return '0000000000000', []

def show_ip_list(ips):
  if ips == []: print([])
  for ip in ips:
    print(ip)

def main():
  for case in xrange(4):
    s, ans = get_input(case)
    res = sorted(compute_all_valid_ip_address(s))
    show_ip_list(res)
    print('Test success' if res == ans else 'Test failure')

if __name__ == '__main__':
  main()
