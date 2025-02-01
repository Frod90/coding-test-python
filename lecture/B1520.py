import sys
sys.setrecursionlimit(99999999)

h, w = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(h)]
visit = [[-1]*w for _ in range(h)]

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def recur(x, y):

  if y == h - 1 and x == w - 1:
    return 1
  if visit[y][x] != -1:
    return visit[y][x]

  count = 0
  for dx, dy in delta:

    if x + dx < 0 or x + dx >= w or y + dy < 0 or y + dy >= h:
      continue
    if graph[y + dy][x + dx] >= graph[y][x]:
      continue

    count += recur(x + dx, y + dy)

  visit[y][x] = count 
  return visit[y][x]

answer = recur(0, 0)
print(answer)
