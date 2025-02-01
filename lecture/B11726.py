
n = int(input())

dp = [0] * n

for i in range(n):

  if i < 2:
    dp[i] = i + 1
  else:
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[-1] % 10_007)