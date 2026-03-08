import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[-1] * (n) for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a - 1][b - 1] = 1
  graph[b - 1][a - 1] = 0
for i in range(n):
  graph[i][i] = 0

for k in range(n):
  for y in range(n):
    for x in range(n):
      if graph[y][k] != -1 and graph[y][k] == graph[k][x]:
        graph[y][x] = graph[y][k]
      
answer = 0
for row in graph:
  if -1 not in row:
    answer += 1
print(answer)