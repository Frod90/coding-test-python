import sys
input = sys.stdin.readline

h, w, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
air_indexs = [y for y in range(h) if graph[y][0] == -1]

directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def counduct_round():
  tmp = [[0] * w for _ in range(h)]
  for y in range(h):
    for x in range(w):
      if graph[y][x] == -1:
        continue

      count = 0
      v = graph[y][x] // 5
      for ex, ey in directs:
        nx, ny = x + ex, y + ey
        if 0 <= nx < w and 0 <= ny < h:
          if graph[ny][nx] != -1:
            tmp[ny][nx] += v
            count += 1
      tmp[y][x] += graph[y][x] - v * count

  auy, ady = air_indexs
  for x in range(1, w):
    graph[auy][x] = tmp[auy][x - 1]
    graph[ady][x] = tmp[ady][x - 1]
  for x in range(w - 1):
    graph[0][x] = tmp[0][x + 1]
    graph[h - 1][x] = tmp[h - 1][x + 1]
  for y in range(auy):
    graph[y][w - 1] = tmp[y + 1][w - 1]
  for y in range(ady + 1, h):
    graph[y][w - 1] = tmp[y - 1][w - 1]
  for y in range(1, auy):
    graph[y][0] = tmp[y - 1][0]
  for y in range(ady + 1, h - 1):
    graph[y][0] = tmp[y + 1][0]

  for y in range(1, h - 1):
    if y == auy or y == ady:
      continue
    for x in range(1, w - 1):
      graph[y][x] = tmp[y][x]

for _ in range(t):
  counduct_round()

auy, ady = air_indexs
graph[auy][0] = 0
graph[ady][0] = 0
answer = sum(sum(row) for row in graph)
print(answer)