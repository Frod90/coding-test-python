import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def cal(nodes):
  dists = [[-1] * n for _ in range(n)]
  directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  q = deque()
  for x, y in nodes:
    dists[y][x] = 0
    q.append((x, y))

  while q:
    bx, by = q.popleft()
    for ex, ey in directs:
      nx, ny = bx + ex, by + ey
      if 0 <= nx < n and 0 <= ny < n:
        if dists[ny][nx] == -1 and graph[ny][nx] != 1:
          dists[ny][nx] = dists[by][bx] + 1
          q.append((nx, ny))

  max_dist = 0
  for y in range(n):
    for x in range(n):
      if graph[y][x] == 0 and dists[y][x] == -1:
        return float('inf')
      
      if graph[y][x] == 2:
        continue
      
      if dists[y][x] > max_dist:
        max_dist = dists[y][x]
  return max_dist

n, m = map(int, input().split())
graph = []
candidates = []
for y in range(n):
  row = list(map(int, input().split()))
  for x in range(n):
    if row[x] == 2:
      candidates.append((x, y))
  graph.append(row)

INF = float('inf')
answer = INF
for combi in combinations(candidates, m):
  answer = min(answer, cal(combi))
print(-1 if answer == INF else answer)
