import math

n = int(input())
nums = list(map(int, input().split()))

counts = [0 for _ in range(n)]
for i in range(1, n):
  n = math.ceil(math.log2(nums[i - 1] / nums[i])) + counts[i - 1]
  counts[i] = max(0, n)

print(sum(counts))