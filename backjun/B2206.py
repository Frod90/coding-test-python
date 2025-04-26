import sys
from collections import deque

input = sys.stdin.readline

h, w = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(h)]
dist = [[[-1, -1] for _ in range(w)] for _ in range(h)]

def _bfs():

  q = deque()
  q.append([0, 0, True])
  dist[0][0][0] = 1

  while q:
    bx, by, bv = q.popleft()

    for ex, ey in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
      nx, ny = bx + ex, by + ey

      if 0 <= nx < w and 0 <= ny < h:

        if bv and graph[ny][nx] == 0 and dist[ny][nx][0] == -1:
          dist[ny][nx][0] = dist[by][bx][0] + 1
          q.append([nx, ny, bv])
        elif not bv and graph[ny][nx] == 0 and dist[ny][nx][1] == -1:
            dist[ny][nx][1] = dist[by][bx][1] + 1
            q.append([nx, ny, bv])
        elif bv and graph[ny][nx] == 1 and dist[ny][nx][1] == -1:
          dist[ny][nx][1] = dist[by][bx][0] + 1
          q.append([nx, ny, False])

_bfs()

res = [d for d in dist[h-1][w-1] if d != -1]
print(min(res) if res else -1)
