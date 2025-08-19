import sys
input = sys.stdin.readline

def cal(n, nums):
  prefix = [0] * (n + 1)
  prefix[0] = nums[0]
  for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + nums[i - 1]

  dp = [[float('inf')] * n for _ in range(n)]
  for i in range(n):
    dp[i][i] = 0
  for i in range(n - 1):
    dp[i][i + 1] = nums[i] + nums[i + 1]

  for dist in range(2, n):
    for y in range(n - dist):
      x = y + dist

      for k in range(y, x):
        dp[y][x] = min(dp[y][x], dp[y][k] + dp[k + 1][x] + prefix[x + 1] - prefix[y])

  return dp[0][-1]

t = int(input())
for _ in range(t):
  n = int(input())
  nums = list(map(int, input().split()))
  print(cal(n, nums))