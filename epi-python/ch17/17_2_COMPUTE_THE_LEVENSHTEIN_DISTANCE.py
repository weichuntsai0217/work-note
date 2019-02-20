from __future__ import print_function

def get_levenstein_distance(sa, sb):
  """
    Time complexity: O(ab), a is the length of sa and b is the length of sb
    Space complexity: O(ab), a is the length of sa and b is the length of sb
  """
  distance_matrix = []
  for i in xrange(len(sa)):
    distance_matrix.append([-1]*len(sb))
  return compute_distance(sa, len(sa) - 1, sb, len(sb) - 1, distance_matrix)

def compute_distance(sa, idxa, sb, idxb, distance_matrix):
  """
  print(sa[0:idxa+1])
  print(sb[0:idxb+1])
  print('==========')
  """
  if idxa < 0:
    return idxb + 1
  if idxb < 0:
    return idxa + 1

  if distance_matrix[idxa][idxb] == -1:
    if sa[idxa] == sb[idxb]:
      distance_matrix[idxa][idxb] = compute_distance(sa, idxa - 1, sb, idxb - 1, distance_matrix)
    else:
      substitute = compute_distance(sa, idxa - 1, sb, idxb - 1, distance_matrix)
      delete_one = compute_distance(sa, idxa - 1, sb, idxb, distance_matrix)
      append_one = compute_distance(sa, idxa, sb, idxb - 1, distance_matrix)
      distance_matrix[idxa][idxb] = 1 + min(substitute, delete_one, append_one)

  return distance_matrix[idxa][idxb]

def main():
  print(get_levenstein_distance('Sundays', 'Sundays') == 0)
  print(get_levenstein_distance('', 'Sundays') == 7)
  print(get_levenstein_distance('Sundays', '') == 7)
  print(get_levenstein_distance('Saturday', 'Sundays') == 4)
  print(get_levenstein_distance('Sundays', 'Saturday') == 4)
  print(get_levenstein_distance('Carthorse', 'Orchestra') == 8)
  print(get_levenstein_distance('Orchestra', 'Carthorse') == 8)
  print(get_levenstein_distance('abc', 'def') == 3)
  print(get_levenstein_distance('abcd', 'aabc') == 2)

if __name__ == '__main__':
  main()
