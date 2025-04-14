import sys
from collections import deque

input = sys.stdin.readline

n, m, h = map(int, input().split())

graph = []
ripeTomatos = []

for i in range(h):

  box = []
  for j in range(m):
    row = list(map(int, input().split()))
    box.append(row)

    for k in range(n):
      if row[k] == 1:
        ripeTomatos.append([k, j, i, 1])

  graph.append(box)

q = deque(ripeTomatos)

while q:
  bx, by, bz, bv = q.popleft()

  for ex, ey, ez in [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]:
    nx, ny, nz = bx + ex, by + ey, bz + ez

    if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
      if graph[nz][ny][nx] == 0:
        graph[nz][ny][nx] = bv + 1
        q.append([nx, ny, nz, bv + 1])

def _calculateAnswer():

  answer = 0
  for box in graph:
    for row in box:

      if 0 in row:
        return -1
      
      answer = max(answer, max(row))

  return answer - 1

print(_calculateAnswer())