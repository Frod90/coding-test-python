from itertools import combinations
from collections import deque

n, m = map(int, input().split())

graph = []
virs = []
zeros = []

for y in range(n):
  row = list(map(int, input().split()))
  graph.append(row)
  for x in range(m):

    if row[x] == 0:
      zeros.append([x, y])

    if row[x] == 2:
      virs.append([x, y])

def _bfs(walls):

  graph02 = [arr[:] for arr in graph]

  for wx, wy in walls:    
    graph02[wy][wx] = 1

  q = deque(virs)
  
  while q:
    bx, by = q.popleft()

    for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      nx, ny = bx + ex, by + ey

      if 0 <= nx < m and 0 <= ny < n:
        if graph02[ny][nx] == 0:
          graph02[ny][nx] = 2
          q.append([nx, ny])

  return sum(row.count(0) for row in graph02)

answer = 0
for walls in combinations(zeros, 3):
  answer = max(answer, _bfs(walls))
print(answer)