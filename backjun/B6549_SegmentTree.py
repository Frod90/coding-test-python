import sys
sys.setrecursionlimit(200000)
from math import log2, ceil
input = sys.stdin.readline

class Seg:

  def build(self, s, e, i):
    if s == e:
      self.tree[i] = s
      return self.tree[i]
    
    mid = (s + e) // 2
    leftMinIndex = self.build(s, mid, i * 2)
    rightMinIndex = self.build(mid + 1, e, i * 2 + 1)

    if self.nums[leftMinIndex] <= self.nums[rightMinIndex]:
      self.tree[i] = leftMinIndex
    else:
      self.tree[i] = rightMinIndex

    return self.tree[i]

  def __init__(self, nums):
    self.nums = nums
    treeSize = 2**(ceil(log2(len(nums))) + 1)
    self.tree = [0] * treeSize
    self.build(0, len(nums) - 1, 1)
  
  def search(self, s, e, l, r, i):
    if r < s or e < l:
      return -1
    
    if l <= s and e <= r:
      return self.tree[i]
    
    mid = (s + e) // 2
    leftMinIndex = self.search(s, mid, l, r, i * 2)
    rightMinIndex = self.search(mid + 1, e, l, r, i * 2 + 1)

    if leftMinIndex == -1:
      return rightMinIndex
    elif rightMinIndex == -1:
      return leftMinIndex

    if self.nums[leftMinIndex] <= self.nums[rightMinIndex]:
      return leftMinIndex
    else:
      return rightMinIndex

  def calculateMaxArea(self, l, r):
    if l > r:
      return 0

    minIndex = self.search(0, len(self.nums) - 1, l, r, 1)
    area = nums[minIndex] * (r - l + 1)
    return max(area, self.calculateMaxArea(l, minIndex - 1), self.calculateMaxArea(minIndex + 1, r))

while True:
  infos = list(map(int, input().split()))
  if infos[0] == 0:
    break

  n, nums = infos[0], infos[1:]
  seg = Seg(nums)
  print(seg.calculateMaxArea(0, n - 1))