import sys
input = sys.stdin.readline
from collections import deque

def mark_island(x, y, island_num):
  q = deque()
  q.append((x, y))
  graph[y][x] = island_num

  while q:
    bx, by = q.popleft()

    for ex, ey in directs:
      nx, ny = bx + ex, by + ey
      if 0 <= nx < n and 0 <= ny < n:
        if graph[ny][nx] == 1:
          graph[ny][nx] = island_num
          q.append((nx, ny))
          
        elif graph[ny][nx] == 0:
          edges.add((bx, by))

def cal():
  q = deque(edges)
  dist = float('inf')

  while q:
    bx, by = q.popleft()

    for ex, ey in directs:
      nx, ny = bx + ex, by + ey
      if 0 <= nx < n and 0 <= ny < n:
        if graph[ny][nx] == 0:
          graph[ny][nx] = graph[by][bx]
          dists[ny][nx] = dists[by][bx] + 1
          q.append((nx, ny))

        elif graph[ny][nx] != graph[by][bx]:
          dist = min(dist, dists[ny][nx] + dists[by][bx])

  return dist

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dists = [[0] * n for _ in range(n)]
directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
edges = set()

island_num = 2
for y in range(n):
  for x in range(n):
    if graph[y][x] == 1:
      mark_island(x, y, island_num)
      island_num += 1

print(cal())