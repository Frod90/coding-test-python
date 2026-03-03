import sys
input = sys.stdin.readline
from collections import deque

def mark():
  directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  visit = [[False] * w for _ in range(h)]
  visit[0][0] = True
  mark_indexs = set()
  q = deque()
  q.append((0, 0))

  while q:
    bx, by = q.popleft()

    for ex, ey in directs:
      nx, ny = bx + ex, by + ey
      if 0 <= nx < w and 0 <= ny < h:
        if graph[ny][nx] == 1:
          mark_indexs.add((nx, ny))
        elif not visit[ny][nx] and graph[ny][nx] == 0:
          visit[ny][nx] = True
          q.append((nx, ny))

  for x, y in mark_indexs:
    graph[y][x] = 0
  return len(mark_indexs)

h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

answer = 0
last = 0
while True:
  tmp = mark()
  if tmp == 0:
    break
  last = tmp
  answer += 1

print(answer)
print(last)