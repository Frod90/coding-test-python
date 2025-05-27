import sys

input = sys.stdin.readline

n, r, c, w = map(int, input().split())

graph = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
dist = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
d = w // 2

for _ in range(n):
  y, x = map(int, input().split())
  graph[y][x] = 1

  sy, ey, sx, ex = max(1, y - d), y + d + 1, max(1, x - d), x + d + 1

  dist[sy][sx] += 1
  if ex <= c:
    dist[sy][ex] -= 1
  if ey <= r:
    dist[ey][sx] -= 1
  if ex <= c and ey <= r:
    dist[ey][ex] += 1

for y in range(r + 1):
  for x in range(1, c + 1):
    dist[y][x] += dist[y][x - 1]
for x in range(c + 1):
  for y in range(1, r + 1):
    dist[y][x] += dist[y - 1][x]

count = 0
point = [0, 0]
for y in range(1, r + 1):
  for x in range(1, c + 1):
    if graph[y][x] == 0:
      if dist[y][x] > count:
        count = dist[y][x]
        point = [y, x]
      elif dist[y][x] == count:
        if y < point[0]:
          point = [y, x]
        elif y == point[0] and x < point[1]:
          point = [y, x]

print(count)
print(*point)
