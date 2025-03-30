import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(m)]
dist = [[10_000 for _ in range(n)] for _ in range(m)]

q = []
heapq.heappush(q, [0, 0, 0])
dist[0][0] = 0

while q:

  v, x, y = heapq.heappop(q)

  if dist[y][x] < v:
    continue

  for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    nx, ny = x + ex, y + ey

    if 0 <= nx < n and 0 <= ny < m:
      if dist[ny][nx] > v + graph[ny][nx]:
        dist[ny][nx] = v + graph[ny][nx]
        heapq.heappush(q, [dist[ny][nx], nx, ny])

print(dist[m - 1][n - 1])