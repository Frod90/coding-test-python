import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y):

  q = deque()
  q.append((x, y, 1))
  visit[y][x] = 1

  while q:
    x, y, count = q.popleft()
    count += 1

    for dx, dy in delta:
      ex, ey = x + dx, y + dy
      if 0 <= ex < w and 0 <= ey < h and graph[ey][ex] == "L" and visit[ey][ex] == 0:
        visit[ey][ex] = count
        q.append((ex, ey, count))

  return count - 1


h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

answer = 0

for x in range(w):
  for y in range(h):

    if graph[y][x] == "W":
      continue
    
    if 0 <= x - 1 and x + 1 < w:
      if graph[y][x - 1] == "L" and graph[y][x + 1] == "L":
        continue
    if 0 <= y - 1 and y + 1 < h:
      if graph[y - 1][x] == "L" and graph[y + 1][x] == "L":
        continue
    
    visit = [[0]*w for _ in range(h)]
    answer = max(answer, bfs(x, y))

print(answer - 1)