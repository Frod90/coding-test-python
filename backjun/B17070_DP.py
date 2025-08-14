import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
  if graph[0][i] == 1:
    break
  
  dp[0][i][0] = 1

for y in range(1, n):
  for x in range(1, n):
    if graph[y][x] == 1:
      continue

    if graph[y - 1][x - 1] == 0 and graph[y - 1][x] == 0 and graph[y][x - 1] == 0:
      dp[y][x][2] += dp[y - 1][x - 1][0]
      dp[y][x][2] += dp[y - 1][x - 1][1]
      dp[y][x][2] += dp[y - 1][x - 1][2]

    dp[y][x][0] += dp[y][x - 1][0] + dp[y][x - 1][2]
    dp[y][x][1] += dp[y - 1][x][1] + dp[y - 1][x][2]

print(sum(dp[-1][-1]))