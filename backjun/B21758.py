import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

prefix = [0] * n
prefix[0] = nums[0]
for i in range(1, n):
  prefix[i] = prefix[i - 1] + nums[i]

answer = 0
for i in range(1, n - 1):
  case1 = (prefix[n - 1] - nums[0] - nums[i]) + (prefix[n - 1] - prefix[i])
  case2 = (prefix[n - 1] - nums[n - 1] - nums[i]) + prefix[i - 1]
  case3 = prefix[n - 1] - nums[0] - nums[n - 1] + nums[i]
  answer = max(answer, case1, case2, case3)
print(answer)