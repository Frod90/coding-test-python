from collections import deque
import sys
input = sys.stdin.readline

w, h = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(h)]

q = deque()
for y in range(h):
  for x in range(w):
    if graph[y][x] == 1:
      q.append([x, y])

while q:
  x, y = q.popleft()

  for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    nx, ny = x + dx, y + dy

    if 0 <= nx < w and 0 <= ny < h:
      if graph[ny][nx] == 0:
        graph[ny][nx] = graph[y][x] + 1
        q.append([nx, ny])

answer = 0
for row in graph:
  if 0 in row:
    answer = 0
    break
  else:
    answer = max(answer, max(row))

print(answer - 1)
