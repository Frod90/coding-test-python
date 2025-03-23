
n = int(input())

graph = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

if n > 2:
  dp[0] = graph[0]
  dp[1] = graph[0] + graph[1]

  for i in range(2, n):
    dp[i] = max(dp[i - 2] + graph[i], dp[i - 3] + graph[i - 1] + graph[i], dp[i - 1])

  print(max(dp))
  
else:
  print(sum(graph))
