n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(2, n + 1):
  dp[i] = min(dp[i], dp[i - 2] + 1)
for i in range(5, n + 1):
  dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[-1] == float('inf'):
  print(-1)
else:
  print(dp[-1])