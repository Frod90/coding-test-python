import sys
input = sys.stdin.readline
from collections import deque

h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
air_graph = [[0] * w for _ in range(h)]
directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def mark():
  q = deque()
  q.append((0, 0))
  visit = [[False] * w for _ in range(h)]

  while q:
    bx, by = q.popleft()

    for ex, ey in directs:
      nx, ny = bx + ex, by + ey

      if 0 <= nx < w and 0 <= ny < h:
        if not visit[ny][nx] and graph[ny][nx] == 0:
          visit[ny][nx] = True
          air_graph[ny][nx] = -1
          q.append((nx, ny))

def dissolve():
  is_dissolved = False
  for y in range(1, h - 1):
    for x in range(1, w - 1):
      if graph[y][x] == 0:
        continue

      air_count = 0
      for ex, ey in directs:
        nx, ny = x + ex, y + ey
        if air_graph[ny][nx] == -1:
          air_count += 1
      
      if air_count >= 2:
        graph[y][x] = 0
        is_dissolved = True
  
  return is_dissolved

answer = 0
is_dissolved = True
while is_dissolved:
  mark()
  is_dissolved = dissolve()
  answer += 1
print(answer - 1)