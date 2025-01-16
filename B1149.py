import sys
input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [[table[0][0], table[0][1], table[0][2]] for _ in range(2)]

for i in range(1, n):

  for j in range(3):
    dp[1][j] = min(dp[0][(j + 1) % 3], dp[0][(j + 2) % 3]) + table[i][j]

  for j in range(3):
    dp[0][j] = dp[1][j]

print(min(dp[1]))