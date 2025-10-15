import sys, heapq
from collections import deque
input = sys.stdin.readline

def bfs(x, y, island_num):
  q = deque()
  q.append((x, y))
  graph[y][x] = island_num

  while q:
    bx, by = q.popleft()

    for ex, ey in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      nx, ny = bx + ex, by + ey
      if 0 <= nx < w and 0 <= ny < h:
        if graph[ny][nx] == 1:
          graph[ny][nx] = island_num
          q.append((nx, ny))

def calculate_length(x, y, island_num):
  delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  for dx, dy in delta:
    nx, ny = x + dx, y + dy
    length = 0
    while 0 <= nx < w and 0 <= ny < h:
      if graph[ny][nx] == 0:
        length += 1
        nx += dx
        ny += dy
        continue
      elif graph[ny][nx] == island_num:
        break
      elif graph[ny][nx] != island_num:
        if length >= 2:
          edges.append((length, graph[ny][nx], island_num))
        break

def _find(a):
  if a == parents[a]:
    return a
  
  parents[a] = _find(parents[a])
  return parents[a]

def _union(a, b):
  parentA, parentB = _find(a), _find(b)
  if parentA == parentB:
    return
  
  if ranks[parentA] > ranks[parentB]:
    parents[parentB] = parentA
  elif ranks[parentB] > ranks[parentA]:
    parents[parentA] = parentB
  else:
    parents[parentA] = parentB
    ranks[parentB] += 1

h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

island_num = 2
for y in range(h):
  for x in range(w):
    if graph[y][x] == 1:
      bfs(x, y, island_num)
      island_num += 1

edges = []
for y in range(h):
  for x in range(w):
    if graph[y][x] != 0:
      calculate_length(x, y, graph[y][x])
heapq.heapify(edges)

parents = [i for i in range(island_num)]
ranks = [0] * island_num
answer = 0
while edges and island_num > 3:
  length, a, b = heapq.heappop(edges)

  if _find(a) == _find(b):
    continue

  answer += length
  _union(a, b)
  island_num -= 1

if island_num == 3:
  print(answer)
else:
  print(-1)