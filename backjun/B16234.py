import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def comb(visit, graph, l, r, x, y):
  if visit[y][x]:
    return False
  
  s = []
  q = deque()
  q.append((x, y))
  visit[y][x] = True
  total = graph[y][x]

  while q:
    bx, by = q.popleft()

    for ex, ey in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      nx, ny = bx + ex, by + ey
      if 0 <= nx < n and 0 <= ny < n:
        if not visit[ny][nx] and l <= abs(graph[by][bx] - graph[ny][nx]) <= r:
          total += graph[ny][nx]
          q.append((nx, ny))
          s.append((nx, ny))
          visit[ny][nx] = True

  if not s:
    return False

  v = total // (len(s) + 1)
  graph[y][x] = v
  for mx, my in s:
    graph[my][mx] = v

  return True

count = 0
while True:
  visit = [[False] * n for _ in range(n)]
  has_move = False
  for y in range(n):
    for x in range(n):
      if comb(visit, graph, l, r, x, y):
        has_move = True

  if not has_move:
    break
  count += 1

print(count)