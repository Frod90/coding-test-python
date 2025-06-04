import sys
from math import log2, ceil

sys.setrecursionlimit(99999999)
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

h = ceil(log2(n)) + 1
tree_size = 2**h

tree = [0 for _ in range(tree_size)]
def _tree(start, end, i):

  if start == end:
    tree[i] = nums[start]
    return tree[i]
  
  mid = (start + end) // 2
  tree[i] = _tree(start, mid, i * 2) + _tree(mid + 1, end, i * 2 + 1)
  return tree[i]
_tree(0, n - 1, 1)

def _search(start, end, left, right, i):

  if end < left or right < start:
    return 0
  
  if left <= start and end <= right:
    return tree[i]
  
  mid = (start + end) // 2
  return _search(start, mid, left, right, i * 2) + _search(mid + 1, end, left, right, i * 2 + 1)

def _update(start, end, baseIdx, diff, i):

  if baseIdx < start or end < baseIdx:
    return
  
  tree[i] += diff

  if start != end:
    mid = (start + end) // 2
    _update(start, mid, baseIdx, diff, i * 2)
    _update(mid + 1, end, baseIdx, diff, i * 2 + 1)

for _ in range(m + k):

  c, a, b = map(int, input().split())

  if c == 1:
    _update(0, n - 1, a - 1, b - nums[a - 1], 1)
    nums[a - 1] = b
  if c == 2:
    print(_search(0, n - 1, a - 1, b - 1, 1))