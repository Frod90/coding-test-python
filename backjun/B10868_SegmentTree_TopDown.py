import sys
input = sys.stdin.readline
from math import log2, ceil

def _tree(start, end, i):
  if start == end:
    tree[i] = nums[start]
    return tree[i]

  mid = (start + end) // 2
  tree[i] = min(_tree(start, mid, i * 2), _tree(mid + 1, end, i * 2 + 1))
  return tree[i]

def _search(start, end, left, right, i):
  if end < left or right < start:
    return INF
  
  if left <= start and end <= right:
    return tree[i]
  
  mid = (start + end) // 2
  return min(_search(start, mid, left, right, i * 2), _search(mid + 1, end, left, right, i * 2 + 1))

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree_size = 2**(ceil(log2(n)) + 1)
INF = float('inf')
tree = [INF] * tree_size
_tree(0, n - 1, 1)

for _ in range(m):
  a, b = map(int, input().split())
  print(_search(0, n - 1, a - 1, b - 1, 1))