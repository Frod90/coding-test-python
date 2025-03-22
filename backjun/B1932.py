
n = int(input())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dp = [[0 for _ in range(i + 1)] for i in range(n - 1)]
dp.append(graph[n - 1])

for y in range(n - 2, -1, -1):
  for x in range(len(dp[y])):
    dp[y][x] = graph[y][x] + max(dp[y + 1][x], dp[y + 1][x + 1])
    
print(dp[0][0])
