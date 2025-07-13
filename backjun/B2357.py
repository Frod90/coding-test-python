import sys
from math import log2, ceil
input = sys.stdin.readline

def maxInit(s, e, i):
  if s == e:
    maxTree[i] = nums[s]
    return maxTree[i]
  
  mid = (s + e) // 2
  maxTree[i] = max(maxInit(s, mid, i * 2), maxInit(mid + 1, e, i * 2 + 1))
  return maxTree[i]

def maxSearch(s, e, l, r, i):
  if e < l or r < s:
    return 0
  
  if l <= s and e <= r:
    return maxTree[i]
  
  mid = (s + e) // 2
  return max(maxSearch(s, mid, l, r, i * 2), maxSearch(mid + 1, e, l, r, i * 2 + 1))

def minInit(s, e, i):
  if s == e:
    minTree[i] = nums[s]
    return minTree[i]
  
  mid = (s + e) // 2
  minTree[i] = min(minInit(s, mid, i * 2), minInit(mid + 1, e, i * 2 + 1))
  return minTree[i]

def minSearch(s, e, l, r, i):
  if e < l or r < s:
    return float('inf')
  
  if l <= s and e <= r:
    return minTree[i]
  
  mid = (s + e) // 2
  return min(minSearch(s, mid, l, r, i * 2), minSearch(mid + 1, e, l, r, i * 2 + 1))

n, m = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]

maxi = 2**(ceil(log2(n)) + 1)
maxTree = [0] * maxi
minTree = [0] * maxi
maxInit(1, n, 1)
minInit(1, n, 1)

for _ in range(m):
  l, r = map(int, input().split())
  print(minSearch(1, n, l, r, 1), maxSearch(1, n, l, r, 1))