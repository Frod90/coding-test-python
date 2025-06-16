import sys
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())
min_dp = [a, b, c]
max_dp = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    min0 = a + min(min_dp[0], min_dp[1])
    min1 = b + min(min_dp[0], min_dp[1], min_dp[2])
    min2 = c + min(min_dp[1], min_dp[2])

    max0 = a + max(max_dp[0], max_dp[1])
    max1 = b + max(max_dp[0], max_dp[1], max_dp[2])
    max2 = c + max(max_dp[1], max_dp[2])

    min_dp = [min0, min1, min2]
    max_dp = [max0, max1, max2]

print(max(max_dp), min(min_dp))