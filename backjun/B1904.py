
n = int(input())

if n >= 2:
  dp = [0 for _ in range(n + 1)]
  dp[1] = 1
  dp[2] = 2

  for i in range(3, n + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
    
  print(dp[-1])

else:
  print(1)