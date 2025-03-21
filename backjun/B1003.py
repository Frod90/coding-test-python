
n = int(input())

dp = [[] for _ in range(41)]

dp[0] = [1, 0]
dp[1] = [0, 1]
for i in range(2, 41):
  a, b = dp[i - 2]
  c, d = dp[i - 1]
  dp[i] = [a + c, b + d]

for _ in range(n):
  print(*dp[int(input())])