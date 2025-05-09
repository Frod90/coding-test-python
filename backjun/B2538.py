import sys
from collections import deque

input = sys.stdin.readline

h, w, k = map(int, input().split())
graph = [[0 for _ in range(w)] for _ in range(h)]

for _ in range(k):
  xa, ya, xb, yb = map(int, input().split())

  for y in range(ya, yb):
    for x in range(xa, xb):
      graph[y][x] = -1

def _bfs(x, y, count):

  q = deque()
  q.append([x, y])
  graph[y][x] = count
  area = 1

  while q:
    bx, by = q.popleft()

    for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      nx, ny = bx + ex, by + ey

      if 0 <= nx < w and 0 <= ny < h:
        if graph[ny][nx] == 0:
          graph[ny][nx] = count
          area += 1
          q.append([nx, ny])

  return area

count = 0
answers = []

for y in range(h):
  for x in range(w):
    if graph[y][x] == 0:
      count += 1
      answers.append(_bfs(x, y, count))

answers.sort()
print(count)
print(*answers)