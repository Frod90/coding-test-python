import sys
from math import log2, ceil
input = sys.stdin.readline

def lazyUpdate(s, e, i):
  if lazy[i] == 0:
    return
  
  if s == e:
    tree[i] += lazy[i]
  else:
    lazy[i * 2] += lazy[i]
    lazy[i * 2 + 1] += lazy[i]

  lazy[i] = 0

def update(s, e, l, r, v, i):
  lazyUpdate(s, e, i)

  if e < l or r < s:
    return  

  if l <= s and e <= r:
    lazy[i] = v
    lazyUpdate(s, e, i)
    return
  
  mid = (s + e) // 2
  update(s, mid, l, r, v, i * 2)
  update(mid + 1, e, l, r, v, i * 2 + 1)

def search(s, e, index, i):
  lazyUpdate(s, e, i)

  if index < s or e < index:
    return 0
  
  if s == e:
    return tree[i]

  mid = (s + e) // 2
  if index <= mid:
    return search(s, mid, index, i * 2)
  else:
    return search(mid + 1, e, index, i * 2 + 1)

n = int(input())
nums = list(map(int, input().split()))

treeLength = 2**(ceil(log2(n)) + 1)
tree = [0] * treeLength
lazy = [0] * treeLength

for i in range(n):
  update(0, n - 1, i, i, nums[i], 1)

m = int(input())
for _ in range(m):
  cmd = list(map(int, input().split()))
  if cmd[0] == 1:
    update(0, n - 1, cmd[1] - 1, cmd[2] - 1, cmd[3], 1)
  else:
    print(search(0, n - 1, cmd[1] - 1, 1))