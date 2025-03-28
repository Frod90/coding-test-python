import sys
input = sys.stdin.readline

import heapq

n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, v = map(int, input().split())
  graph[a].append([b, v])

def calc(start):

  dist = [10_000_000 for _ in range(n + 1)]
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

answers = calc(k)
for i in range(1, n + 1):
  tmp = calc(i)
  answers[i] += tmp[k]

answers[0] = 0
print(max(answers))