import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, v = map(int, input().split())
  graph[a].append([b, v])
  graph[b].append([a, v])

maxi = 160_000_000
def calc(start):

  dist = [maxi for _ in range(n + 1)]
  q = []
  heapq.heappush(q, [0, start])
  dist[start] = 0

  while q:
    v, b = heapq.heappop(q)

    if dist[b] < v:
      continue

    for nb, ev in graph[b]:
      nv = v + ev

      if dist[nb] > nv:
        dist[nb] = nv
        heapq.heappush(q, [nv, nb])

  return dist

v1, v2 = map(int, input().split())

startDist = calc(1)
b = calc(v1)[v2]
endDist = calc(n)

answer = min(
  startDist[v1] + b + endDist[v2],
  startDist[v2] + b + endDist[v1]
  )

if answer >= maxi:
  print(-1)
else:
  print(answer)