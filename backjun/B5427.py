import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
INF = float('inf')

def cal():
  w, h = map(int, input().split())
  graph = []
  q = deque()
  dists = [[INF] * w for _ in range(h)]
  fires = deque()

  for y in range(h):
    row = list(input().rstrip())
    for x in range(w):
      if row[x] == '@':
        q.append((x, y))
        dists[y][x] = 0
      elif row[x] == '*':
        fires.append((x, y))
    graph.append(row)

  while q:
    fn = len(fires)
    for _ in range(fn):
      x, y = fires.popleft()
      for ex, ey in directs:
        fx, fy = x + ex, y + ey
        if 0 <= fx < w and 0 <= fy < h and graph[fy][fx] == '.':
          graph[fy][fx] = '*'
          fires.append((fx, fy))

    qn = len(q)
    for _ in range(qn):
      bx, by = q.popleft()
      for ex, ey in directs:
        nx, ny = bx + ex, by + ey
        if nx < 0 or w <= nx or ny < 0 or h <= ny:
          return dists[by][bx] + 1
        elif graph[ny][nx] == '.' and dists[ny][nx] == INF:
          dists[ny][nx] = dists[by][bx] + 1
          q.append((nx, ny))

  return -1
  
for _ in range(t):
  answer = cal()
  print(answer if answer != -1 else "IMPOSSIBLE")