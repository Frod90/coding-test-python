import sys
from math import ceil, log2

sys.setrecursionlimit(9999999)
input = sys.stdin.readline

division_unit = 1_000_000_007
n, m, k = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]

h = ceil(log2(n)) + 1
tree_size = 2**h
tree = [1 for _ in range(tree_size)]
leafNodeIdxs = [0 for _ in range(n + 1)]

def _tree(start, end, i):

  if start == end:
    tree[i] = nums[start]
    leafNodeIdxs[start] = i
    return tree[i]

  mid = (start + end) // 2
  tree[i] = (_tree(start, mid, i * 2) * _tree(mid + 1, end, i * 2 + 1)) % division_unit
  return tree[i]

_tree(1, n, 1)

def _update(start, end, value, idx, i):

  if idx < start or end < idx:
    return tree[i]
  
  if start == end:
    tree[i] = value
    return tree[i]
  
  mid = (start + end) // 2
  tree[i] = (_update(start, mid, value, idx, i * 2) * _update(mid + 1, end, value, idx, i * 2 + 1)) % division_unit
  return tree[i]

def _search(start, end, left, right, i):

  if right < start or end < left:
    return 1
  
  if left <= start and end <= right:
    return tree[i]
  
  mid = (start + end) // 2
  return (_search(start, mid, left, right, i * 2) * _search(mid + 1, end, left, right, i * 2 + 1)) % division_unit

for _ in range(m + k):
  a, b, c = map(int, input().split())

  if a == 1:
    _update(1, n, c, b, 1)
  else:
    print(_search(1, n, b, c, 1))