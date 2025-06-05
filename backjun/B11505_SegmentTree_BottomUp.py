import sys
from math import log2, ceil

input = sys.stdin.readline

division_unit = 1_000_000_007
n, m ,k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

h = ceil(log2(n))
leafNodeSize = 2**h
tree = [1 for _ in range(leafNodeSize * 2)]

def _update(value, i):

  i += leafNodeSize
  tree[i] = value
  i //= 2

  while i:
    tree[i] = (tree[i * 2] * tree[i * 2 + 1]) % division_unit
    i //= 2

def _search(left, right):

  left += leafNodeSize
  right += leafNodeSize
  tmp = 1

  while left <= right:

    if left % 2 == 1:
      tmp = (tmp * tree[left]) % division_unit
      left += 1
    left //= 2

    if right % 2 == 0:
      tmp = (tmp * tree[right]) % division_unit
      right -= 1
    right //= 2
  
  return tmp % division_unit

for i in range(n):
  _update(nums[i], i)

for _ in range(m + k):
  a, b, c = map(int, input().split())

  if a == 1:
    _update(c, b - 1)
  else:
    print(_search(b - 1, c - 1))