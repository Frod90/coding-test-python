import sys
from math import log2, ceil
input = sys.stdin.readline

def init(s, e, i):
  if s == e:
    tree[i] = nums[s]
    return tree[i]
  
  mid = (s + e) // 2
  tree[i] = init(s, mid, i * 2) ^ init(mid + 1, e, i * 2 + 1)
  return tree[i]

def lazyUpdate(s, e, i):
  if lazy[i] == 0:
    return
  
  if (e - s + 1) % 2 == 1:
    tree[i] ^= lazy[i]
  
  if s != e:
    lazy[i * 2] ^= lazy[i]
    lazy[i * 2 + 1] ^= lazy[i]

  lazy[i] = 0

def update(s, e, l, r, v, i):
  lazyUpdate(s, e, i)

  if e < l or r < s:
    return tree[i]
  
  if l <= s and e <= r:
    lazy[i] ^= v
    lazyUpdate(s, e, i)
    return tree[i]
  
  mid = (s + e) // 2
  tree[i] = update(s, mid, l, r, v, i * 2) ^ update(mid + 1, e, l, r, v, i * 2 + 1)
  return tree[i]

def search(s, e, l, r, i):
  lazyUpdate(s, e, i)

  if e < l or r < s:
    return 0
  
  if l <= s and e <= r:
    return tree[i]
  
  mid = (s + e) // 2
  return search(s, mid, l, r, i * 2) ^ search(mid + 1, e, l, r, i * 2 + 1)

n = int(input())
nums = list(map(int, input().split()))

treeLength = 2**(ceil(log2(n)) + 1)
tree = [0] * treeLength
lazy = [0] * treeLength
init(0, n - 1, 1)

m = int(input())
for _ in range(m):
  
  cmd = list(map(int, input().split()))
  if cmd[0] == 1:
    update(0, n - 1, cmd[1], cmd[2], cmd[3], 1)
  else:
    print(search(0, n - 1, cmd[1], cmd[2], 1))