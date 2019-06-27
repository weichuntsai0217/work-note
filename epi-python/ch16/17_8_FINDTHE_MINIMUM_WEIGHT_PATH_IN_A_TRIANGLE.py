from __future__ import print_function

def get_min_weight_path(triangle):
  res = [] # res = [{'sum': 2, seq:[]}, ...]
  for col_idx, col_val in enumerate(triangle[0]):
    res.append({
      'sum': col_val,
      'seq': [col_idx],
    })

  for row_idx in xrange(1, len(triangle)):
    dst_row = triangle[row_idx]
    tmp = []
    for i in xrange(len(dst_row)):
      tmp.append({
        'sum': float('inf'),
        'seq': [],    
      })
    for col_idx in xrange(len(res)):
      first_sum = dst_row[col_idx] + res[col_idx]['sum']
      if first_sum < tmp[col_idx]['sum']:
        tmp[col_idx]['sum'] = first_sum
        tmp[col_idx]['seq'] = res[col_idx]['seq'] + [col_idx]
        
      second_sum = dst_row[col_idx+1] + res[col_idx]['sum']
      if second_sum < tmp[col_idx+1]['sum']:
        tmp[col_idx+1]['sum'] = second_sum
        tmp[col_idx+1]['seq'] = res[col_idx]['seq'] + [col_idx+1]

    res = tmp
  # print(res)
  min_item = {
    'sum': float('inf'),
    'seq': [],
  }
  for item in res:
    if item['sum'] < min_item['sum']:
      min_item['sum'] = item['sum']
      min_item['seq'] = item['seq']
  return min_item

def get_input():
  triangle = [
    [2],
    [4, 4],
    [8, 5, 6],
    [4, 2, 6, 2],
    [1, 5, 2, 3, 4],
  ]
  ans = {
    'sum': 15,
    'seq': [0, 0, 1, 1, 2]
  }
  return triangle, ans

def main():
  triangle, ans = get_input()
  res = get_min_weight_path(triangle)
  print('Test success' if res['sum'] == ans['sum'] and res['seq'] == ans['seq'] else 'Test failure')

if __name__ == '__main__':
  main()
