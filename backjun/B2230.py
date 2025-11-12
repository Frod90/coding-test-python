import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

i, j = 0, 1
answer = float('inf')
while i < n and j < n:
  if nums[j] - nums[i] < m:
    j += 1
  else:
    answer = min(answer, nums[j] - nums[i])
    i += 1

print(answer)