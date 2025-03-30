import sys
input = sys.stdin.readline

import heapq

count = 0
while True:

  n = int(input())
  if n == 0:
    break

  count += 1
  graph = [list(map(int, input().split())) for _ in range(n)]
  dist = [[300_000 for _ in range(n)] for _ in range(n)]

  q = []
  heapq.heappush(q, [graph[0][0], 0, 0])
  dist[0][0] = graph[0][0]

  while q:
    v, x, y = heapq.heappop(q)

    if dist[y][x] < v:
      continue

    for ex, ey in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
      nx, ny = x + ex, y + ey

      if 0 <= nx < n and 0 <= ny < n:
        nv = v + graph[ny][nx]

        if dist[ny][nx] > nv:
          dist[ny][nx] = nv
          heapq.heappush(q, [nv, nx, ny])
  
  print("Problem " + str(count) + ":", dist[n - 1][n - 1])