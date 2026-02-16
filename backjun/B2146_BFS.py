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

def cal(num):
  dists = [[-1] * n for _ in range(n)]
  q = deque()
  for y in range(n):
    for x in range(n):
      if graph[y][x] == num:
        q.append((x, y))
        dists[y][x] = 0
  
  while q:
    bx, by = q.popleft()

    for ex, ey in directs:
      nx, ny = bx + ex, by + ey
      if 0 <= nx < n and 0 <= ny < n:
        if graph[ny][nx] > 0 and graph[ny][nx] != num:
          return dists[by][bx]
        if graph[ny][nx] == 0 and dists[ny][nx] == -1:
          dists[ny][nx] = dists[by][bx] + 1
          q.append((nx, ny))

  return float('inf')

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

island_num = 2
for y in range(n):
  for x in range(n):
    if graph[y][x] == 1:
      mark_island(x, y, island_num)
      island_num += 1

answer = float('inf')
for num in range(2, island_num):
  answer = min(answer, cal(num))
print(answer)