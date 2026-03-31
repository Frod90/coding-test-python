import sys
input = sys.stdin.readline
from collections import deque

h, w = map(int, input().split())
graph = []
target_x, target_y = -1, -1
start_x, start_y = -1, -1
waters = deque()
for y in range(h):
  row = list(input().rstrip())
  for x in range(w):
    if row[x] == 'D':
      target_x, target_y = x, y
    elif row[x] == 'S':
      start_x, start_y = x, y
      row[x] = '.'
    elif row[x] == '*':
      waters.append((x, y))
  
  graph.append(row)

directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()
q.append((start_x, start_y))
dist = 0
visit = [[False] * w for _ in range(h)]
visit[start_y][start_x] = True

while q:
  for _ in range(len(waters)):
    wx, wy = waters.popleft()
    for ex, ey in directs:
      wnx, wny = wx + ex, wy + ey
      if 0 <= wnx < w and 0 <= wny < h and graph[wny][wnx] == '.':
        graph[wny][wnx] = '*'
        waters.append((wnx, wny))
  
  dist += 1
  for _ in range(len(q)):
    bx, by = q.popleft()

    for ex, ey in directs:
      nx, ny = bx + ex, by + ey

      if nx == target_x and ny == target_y:
        print(dist)
        exit()

      if 0 <= nx < w and 0 <= ny < h and not visit[ny][nx] and graph[ny][nx] == '.':
        visit[ny][nx] = True
        q.append((nx, ny))

print("KAKTUS")