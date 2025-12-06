
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(h)]
dists = [[0] * w for _ in range(h)]

for y in range(h):
  dists[y][0] = graph[y][0]
for x in range(w):
  dists[0][x] = graph[0][x]

for y in range(1, h):
  for x in range(1, w):
    if graph[y][x]:
      dists[y][x] = min(dists[y - 1][x], dists[y][x - 1], dists[y - 1][x - 1]) + 1

print(max(max(row) for row in dists)**2)