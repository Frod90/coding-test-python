import sys
input = sys.stdin.readline

import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, v = map(int, input().split())
  graph[a].append([b, v])

route = [i for i in range(n + 1)]
dist = [100_000_000 for _ in range(n + 1)]

s, e = map(int, input().split())

q = []
heapq.heappush(q, [0, s])
dist[s] = 0 

while q:
  v, b = heapq.heappop(q)

  if dist[b] < v:
    continue

  for nb, ev in graph[b]:
    nv = v + ev

    if dist[nb] > nv:
      dist[nb] = nv
      heapq.heappush(q, [nv, nb])
      route[nb] = b

answerRoute = [e]
idx = e
while idx != s:
  answerRoute.append(route[idx])
  idx = route[idx]

print(dist[e])
print(len(answerRoute))
print(*answerRoute[::-1])