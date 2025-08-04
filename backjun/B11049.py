import sys
input = sys.stdin.readline

n = int(input())
matrixs = [list(map(int, input().split())) for _ in range(n)]
p = [matrixs[i][0] for i in range(n)] + [matrixs[-1][1]]
dp = [[float('inf')] * n for _ in range(n)]
for i in range(n):
  dp[i][i] = 0

for dist in range(1, n):
  for i in range(n - dist):
    j = i + dist
    if dist == 1:
      dp[i][j] = p[i] * p[i + 1] * p[j + 1]
      continue

    for k in range(i, j):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1])

print(dp[0][-1])