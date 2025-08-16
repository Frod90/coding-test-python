n, k = map(int, input().split())

dp = [[0] * (n + 1) for _ in range(k + 1)]
for i in range(n + 1):
  dp[1][i] = 1
for j in range(1, k + 1):
  dp[j][0] = 1

for y in range(2, k + 1):
  for x in range(1, n + 1):
    dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % 1_000_000_000

print(dp[-1][-1])