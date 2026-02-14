import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

visit = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]
directs_next = [(1, 0), (-1, 0), (0, 1), (0, -1)]
directs_hourse = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

q = deque()
q.append((0, 0, 0, 0))
answer = -1
while q:
  bx, by, used, dist = q.popleft()
  if bx == w - 1 and by == h - 1:
    answer = dist
    break

  for ex, ey in directs_next:
    nx, ny = bx + ex, by + ey
    if 0 <= nx < w and 0 <= ny < h:
      if graph[ny][nx] == 0 and not visit[ny][nx][used]:
        visit[ny][nx][used] = True
        q.append((nx, ny, used, dist + 1))
  
  if used < k:
    for ex, ey in directs_hourse:
      nx, ny = bx + ex, by + ey
      if 0 <= nx < w and 0 <= ny < h:
        if graph[ny][nx] == 0 and not visit[ny][nx][used + 1]:
          visit[ny][nx][used + 1] = True
          q.append((nx, ny, used + 1, dist + 1))

print(answer)