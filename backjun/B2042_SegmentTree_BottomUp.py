import sys
from math import ceil, log2

input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

treeSize = 2 ** (ceil(log2(n)) + 1)

tree = [0 for _ in range(treeSize)]

def _update(diff, i):
  i += treeSize // 2
  while i:
    tree[i] += diff
    i //= 2

for i in range(n):
  _update(nums[i], i)

def _search(start, end):

  start += treeSize // 2
  end += treeSize // 2
  tmp = 0

  while start <= end:

    if start % 2 == 1:
      tmp += tree[start]
      start += 1
    start //= 2

    if end % 2 == 0:
      tmp += tree[end]
      end -= 1
    end //= 2

  return tmp

for _ in range(m + k):

  a, b, c = map(int, input().split())

  if a == 1:
    _update(c - nums[b - 1], b - 1)
    nums[b - 1] = c
  else:
    print(_search(b - 1, c - 1))
