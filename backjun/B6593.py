import sys
input = sys.stdin.readline
from collections import deque

directs = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

while True:
  h, d, w = map(int, input().split())
  if h == 0 and d == 0 and w == 0:
    break
  
  start = []
  end = []
  graph = []
  for z in range(h):
    floor = []
    for y in range(d):
      row = list(input().rstrip())
      floor.append(row)

      for x in range(w):
        if row[x] == 'S':
          start = (x, y, z)

    graph.append(floor)
    input()

  dists = [[[-1] * w for _ in range(d)] for _ in range(h)]
  q = deque()
  q.append(start)
  dists[start[2]][start[1]][start[0]] = 0

  answer = "Trapped!"
  while q:
    bx, by, bz = q.popleft()
    if graph[bz][by][bx] == 'E':
      answer = "Escaped in " + str(dists[bz][by][bx]) + " minute(s)."
      break

    for ex, ey, ez in directs:
      nx, ny, nz = bx + ex, by + ey, bz + ez

      if 0 <= nx < w and 0 <= ny < d and 0 <= nz < h:
        if graph[nz][ny][nx] != '#' and dists[nz][ny][nx] == -1:
          dists[nz][ny][nx] = dists[bz][by][bx] + 1
          q.append((nx, ny, nz))

  print(answer)