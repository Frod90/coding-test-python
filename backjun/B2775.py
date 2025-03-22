
n = int(input())

for _ in range(n):

  a = int(input())
  b = int(input())

  dp = [[1 for _ in range(b)] for _ in range(a + 1)]
  for i in range(b):
    dp[0][i] = i + 1

  for y in range(1, a + 1):
    for x in range(1, b):
      dp[y][x] = dp[y][x - 1] + dp[y - 1][x]

  print(dp[a][b - 1])
