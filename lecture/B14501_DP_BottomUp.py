import sys
sys.setrecursionlimit(99999999)

input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n)[::-1]:

  if i + table[i][0] > n:
    dp[i] = dp[i + 1]
  else:
    dp[i] = max(dp[i + table[i][0]] + table[i][1], dp[i + 1])

print(dp[0])
