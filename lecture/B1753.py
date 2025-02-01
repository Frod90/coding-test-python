import sys
input = sys.stdin.readline

import heapq

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
  u, v, w = map(int, input().split())
  graph[u].append([v, w])

maxi = V * 10 + 1
dist = [maxi] * (V + 1)
dist[K] = 0

q = []
heapq.heappush(q, [0, K])

while q:

  value, index = heapq.heappop(q)

  for v, w in graph[index]:
    if value + w < dist[v]:
      dist[v] = value + w
      heapq.heappush(q, [dist[v], v])

for i in range(1, V + 1):
  if dist[i] == maxi:
    print("INF")
  else:
    print(dist[i])