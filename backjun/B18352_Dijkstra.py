import sys
input = sys.stdin.readline

import heapq

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

dist = [300_000_000_000 for _ in range(n + 1)]

q = []
heapq.heappush(q, [0, x])
dist[x] = 0

while q:
  v, b = heapq.heappop(q)

  if v > k:
    break

  if dist[b] < v:
    continue

  for nb in graph[b]:
    if dist[nb] > v + 1:
      dist[nb] = v + 1
      heapq.heappush(q, [v + 1, nb])

isNothing = True
for i in range(1, n + 1):
  if dist[i] == k:
    print(i)
    isNothing = False
if isNothing:
  print(-1)