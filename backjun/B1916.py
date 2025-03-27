import sys
input = sys.stdin.readline

import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, v = map(int, input().split())
  graph[a].append([v, b])

s, e = map(int, input().split())

dist = [1_000_000_000 for _ in range(n + 1)]

q = []
heapq.heappush(q, [0, s])
dist[s] = 0

while q:
  v, b = heapq.heappop(q)

  if dist[b] < v:
    continue

  for ev, nb in graph[b]:
    nv = v + ev

    if nv < dist[nb]:
      dist[nb] = nv
      heapq.heappush(q, [nv, nb])

print(dist[e])