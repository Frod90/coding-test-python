import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

heights = set()
graph = []
idxs = [[] for _ in range(101)]

for y in range(n):

  row = list(map(int, input().split()))

  for x in range(n):
    idxs[row[x]].append([x, y])
  graph.append(row)
  heights.update(row)

visit = [[True for _ in range(n)] for _ in range(n)]

def _calc():

  dist = [[-1 for _ in range(n)] for _ in range(n)]

  q = deque()

  count = 0
  for y in range(n):
    for x in range(n):

      if visit[y][x] and dist[y][x] == -1:
        count += 1
        q.append([x, y])

      while q:
        bx, by = q.popleft()

        for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
          nx, ny = bx + ex, by + ey

          if 0 <= nx < n and 0 <= ny < n:
            if visit[ny][nx] and dist[ny][nx] == -1:
              dist[ny][nx] = count
              q.append([nx, ny])

  return count

def _func(height):

  for x, y in idxs[height]:
    visit[y][x] = False

answer = 1

for height in heights:
  _func(height)
  answer = max(answer, _calc())

print(answer)