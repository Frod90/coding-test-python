import sys
input = sys.stdin.readline

n = int(input())

graph = [int(input()) for _ in range(n)]

if n <= 2:
  print(sum(graph))
else:
  dp = [0 for _ in range(n)]

  dp[0] = graph[0]
  dp[1] = graph[0] + graph[1]

  for i in range(2, n):
    dp[i] = graph[i] + max(graph[i - 1] + dp[i - 3], dp[i - 2])

  print(dp[n - 1])