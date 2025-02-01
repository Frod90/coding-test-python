import sys
sys.setrecursionlimit(99999999)

input = sys.stdin.readline

n, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):

  weight = table[i][0]
  value = table[i][1]

  for j in range(0, k + 1):

    if j < weight:
      dp[i + 1][j] = dp[i][j]
    else:
      dp[i + 1][j] = max(dp[i][j - weight] + value, dp[i][j])

print(dp[n][k])