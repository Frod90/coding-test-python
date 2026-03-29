import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = float('inf')
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  a, b, v = map(int, input().split())
  graph[a][b] = v

for k in range(1, n + 1):
  for y in range(1, n + 1):
    for x in range(1, n + 1):
      new_dist = graph[y][k] + graph[k][x]
      if new_dist < graph[y][x]:
        graph[y][x] = new_dist

answer = INF
for i in range(1, n + 1):
  answer = min(answer, graph[i][i])

print(answer if answer != INF else -1)