import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * n for _ in range(n)]
dist[-1][-1] = 1

for y in range(n - 1, -1, -1):
  for x in range(n - 1, -1, -1):
    delta = graph[y][x]
    if delta == 0:
      continue

    if x + delta < n:
      dist[y][x] += dist[y][x + delta]
    if y + delta < n:
      dist[y][x] += dist[y + delta][x]

print(dist[0][0])