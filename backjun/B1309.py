n = int(input())
dp = [1] * 3

for i in range(1, n):
  v1 = (dp[0] + dp[1] + dp[2]) % 9901
  v2 = (dp[0] + dp[2]) % 9901
  v3 = (dp[0] + dp[1]) % 9901
  dp = [v1, v2, v3]

print(sum(dp) % 9901)