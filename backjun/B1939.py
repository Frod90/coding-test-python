import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append([b, -c])
  graph[b].append([a, -c])

dist = [0 for _ in range(n + 1)]
q = []

s, e = map(int, input().split())
heapq.heappush(q, [-1_000_000_000, s])
dist[s] = -1_000_000_000

while q:

  v, b = heapq.heappop(q)

  if v > dist[b]:
    continue

  for nb, ev in graph[b]:
    nv = max(v, ev)

    if nv < dist[nb]:
      dist[nb] = nv
      heapq.heappush(q, [nv, nb])

print(-dist[e])