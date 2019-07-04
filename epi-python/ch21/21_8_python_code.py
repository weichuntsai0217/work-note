"""
  Use python 3.6.8
"""
import functools
import heapq
import collections

def compute_top_k_variance(students, scores, k):
  pairs = zip(students, scores)
  all_scores = collections.defaultdict(list)
  for stu, sco in pairs:
    all_scores[stu].append(sco)

  top_k_scores = {
    stu: heapq.nlargest(k, scos)
    for stu, scos in all_scores.items() if len(scos) >= k
  }

  return {
    stu: functools.reduce(lambda tot, x: tot + (x - mean)**2, scos, 0)
    for stu, scos, mean in ((stu, scos, sum(scos)/k) for stu, scos in top_k_scores.items())
  }

def main():
  students = ['A', 'B', 'A', 'C', 'B', 'B', 'A', 'C', 'B', 'A']
  scores = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
  k = 3
  print(compute_top_k_variance(students, scores, k))

if __name__ == '__main__':
  main()
