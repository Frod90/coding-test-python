import sys
from math import log2, ceil
from bisect import bisect_right
input = sys.stdin.readline

def init(s, e, i):
  tree[i] = sorted(nums[s:e + 1])
  
  if s == e:
    return

  mid = (s + e) // 2
  init(s, mid, i * 2)
  init(mid + 1, e, i * 2 + 1)

def search(s, e, l, r, v, i):
  if e < l or r < s:
    return 0
  
  if l <= s and e <= r:
    return bisect_right(tree[i], v)
  
  mid = (s + e) // 2
  return search(s, mid, l, r, v, i * 2) + search(mid + 1, e, l, r, v, i * 2 + 1)

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))

maxi = 2**(ceil(log2(n)) + 1)
tree = [[]] * maxi
init(1, n, 1)

for _ in range(m):
  left, right, k = map(int, input().split())
  high, row = 1_000_000_000, -1_000_000_000

  while row <= high:
    mid = (row + high) // 2
    c = search(1, n, left, right, mid, 1)
    if c < k:
      row = mid + 1
    else:
      high = mid - 1

  print(row)