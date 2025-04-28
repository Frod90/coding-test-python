import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
sy, sx, sd = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
visit[sy][sx] = True

delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def _recur(x, y, i, count):

  if x < 0 or m <= x or y < 0 or n <= y:
    return count
  
  if graph[y][x] == 1:
    return count

  for di in range(1, 5):
    tmpIdx = (i + di * 3) % 4
    dx, dy = delta[tmpIdx]
    nx, ny = x + dx, y + dy

    if 0 <= nx < m and 0 <= ny < n:
      if graph[ny][nx] == 0 and not visit[ny][nx]:
        visit[ny][nx] = True
        return _recur(nx, ny, tmpIdx, count + 1)
      
  ex, ey = delta[i]
  return _recur(x - ex, y - ey, i, count)

print(_recur(sx, sy, sd, 1))