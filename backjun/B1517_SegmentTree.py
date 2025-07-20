import sys
from math import log2, ceil
input = sys.stdin.readline

def search(l, r):
  l += size
  r += size
  c = 0

  while l <= r:
    if l % 2 == 1:
      c += tree[l]
      l += 1
    l //= 2

    if r % 2 == 0:
      c += tree[r]
      r -= 1
    r //= 2
  
  return c

def update(index, value):
  index += size
  tree[index] += value
    
  while index > 1:
    tree[index // 2] = tree[index] + tree[index ^ 1]
    index //= 2

n = int(input())
nums = list(map(int, input().split()))

comp = {}
for i, cn in enumerate(set(sorted(nums))):
  comp[cn] = i

comp_size = len(comp)
size = 2**(ceil(log2(comp_size)))
tree = [0] * (size * 2)

count = 0
for num in nums:
  index = comp[num]
  if index + 1 < comp_size:
    count += search(index + 1, comp_size - 1)
  update(index, 1)

print(count)