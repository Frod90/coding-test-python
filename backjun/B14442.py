import sys
input = sys.stdin.readline
from collections import deque

h, w, k = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(h)]

INF = float('inf')
dists = [[[INF] * (k + 1) for _ in range(w)] for _ in range(h)]
dists[0][0][0] = 1

q = deque()
q.append((0, 0, 0))
directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

answer = -1
while q:
  bx, by, bk = q.popleft()
  if bx == w - 1 and by == h - 1:
    answer = dists[by][bx][bk]
    break

  for ex, ey in directs:
    nx, ny = bx + ex, by + ey
    
    if 0 <= nx < w and 0 <= ny < h:
      if graph[ny][nx] == 0 and dists[ny][nx][bk] == INF:
        dists[ny][nx][bk] = dists[by][bx][bk] + 1
        q.append((nx, ny, bk))
      elif graph[ny][nx] == 1 and bk < k and dists[ny][nx][bk + 1] == INF:
        dists[ny][nx][bk + 1] = dists[by][bx][bk] + 1
        q.append((nx, ny, bk + 1))
print(answer)