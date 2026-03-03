import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

ab_set = set()
for a in nums:
  for b in nums:
    ab_set.add(a + b)

for i in range(n - 1, -1, -1):
  k = nums[i]

  for c in nums:
    if k - c in ab_set:
      print(k)
      exit()