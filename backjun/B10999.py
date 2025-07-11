import sys
from math import log2, ceil
input = sys.stdin.readline

def init(s, e, i):
  if s == e:
    tree[i] = nums[s]
    return tree[i]

  mid = (s + e) // 2
  tree[i] = init(s, mid, i * 2) + init(mid + 1, e, i * 2 + 1)
  return tree[i]

def lazyUpdate(s, e, i):
  if lazy[i] == 0:
    return
  
  tree[i] += (e - s + 1) * lazy[i]
  
  if s != e:
    lazy[i * 2] += lazy[i]
    lazy[i * 2 + 1] += lazy[i]
  
  lazy[i] = 0

def search(s, e, l, r, i):
  lazyUpdate(s, e, i)

  if e < l or r < s:
    return 0
  
  if l <= s and e <= r:
    return tree[i]
  
  mid = (s + e) // 2
  return search(s, mid, l, r, i * 2) + search(mid + 1, e, l, r, i * 2 + 1)

def update(s, e, l, r, diff, i):
  lazyUpdate(s, e, i)
  
  if e < l or r < s:
    return tree[i]
  
  if l <= s and e <= r:
    lazy[i] = diff
    lazyUpdate(s, e, i)
    return tree[i]

  mid = (s + e) // 2
  tree[i] = update(s, mid, l, r, diff, i * 2) + update(mid + 1, e, l, r, diff, i * 2 + 1)
  return tree[i]

n, m, k = map(int, input().split())

nums = [int(input()) for _ in range(n)]

maxi = 2**(ceil(log2(n)) + 1)
tree = [0] * maxi
lazy = [0] * maxi

init(0, n - 1, 1)

for _ in range(m + k):
  cmds = list(map(int, input().split()))

  if cmds[0] == 1:
    update(0, n - 1, cmds[1] - 1, cmds[2] - 1, cmds[3], 1)
  if cmds[0] == 2:
    print(search(0, n - 1, cmds[1] - 1, cmds[2] - 1, 1))