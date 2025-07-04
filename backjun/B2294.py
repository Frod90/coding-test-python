import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] + [float('inf')] * k

for coin in coins:
  for i in range(coin, k + 1):
    dp[i] = min(dp[i], dp[i - coin] + 1)
    
if dp[k] == float('inf'):
  print(-1)
else:
  print(dp[k])