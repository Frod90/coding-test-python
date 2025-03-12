from collections import deque

h, w = map(int, input().split())

graph = []

for i in range(h):
  graph.append(list(map(int, list(input()))))

dist = [[0 for _ in range(w)] for _ in range(h)]
dist[0][0] = 1

q = deque()
q.append([0, 0])

while q:
  x, y = q.popleft()

  for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:

    nx, ny = x + dx, y + dy

    if 0 <= nx < w and 0 <= ny < h:
      if graph[ny][nx] == 1 and dist[ny][nx] == 0:
        dist[ny][nx] = dist[y][x] + 1
        q.append([nx, ny])

print(dist[h - 1][w - 1])
