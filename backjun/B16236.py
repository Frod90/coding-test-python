import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
points = []
sp = [2, 0, 0, 0]

for y in range(n):

  row = list(map(int, input().split()))
  graph.append(row)

  for x in range(n):
    if row[x] == 9:
      sp[2], sp[3] = x, y
      graph[y][x] = 0

def _isFindNextPoint(sx, sy, value):

  dists = [[0 for _ in range(n)] for _ in range(n)]
  dists[sy][sx] = 1
  q = deque()
  q.append([sx, sy])
  nodes = []

  while q:

    bx, by = q.popleft()
    
    for ex, ey in [[0, -1], [-1, 0], [1, 0], [0, 1]]:
      nx, ny = bx + ex, by + ey

      if 0 <= nx < n and 0 <= ny < n:
        if graph[ny][nx] != 0 and graph[ny][nx] < value:
          dists[ny][nx] = dists[by][bx] + 1
          nodes.append([dists[by][bx], nx, ny])
        
        elif dists[ny][nx] == 0 and graph[ny][nx] <= value:
          dists[ny][nx] = dists[by][bx] + 1
          q.append([nx, ny])

  if not nodes:
    return -1

  nodes.sort(key=lambda x: (x[0], x[2], x[1]))
  for count, x, y in nodes:
    sp[2], sp[3] = x, y
    sp[1] += 1
    graph[y][x] = 0

    return count
    
count = 0
while True:

  tmpCount = _isFindNextPoint(sp[2], sp[3], sp[0])
  if tmpCount == -1:
    break

  count += tmpCount
  if sp[0] == sp[1]:
    sp[0] += 1
    sp[1] = 0

print(count)