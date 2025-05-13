import sys
import heapq

input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(r):
  a, b, v = map(int, input().split())
  graph[a - 1].append([b - 1, v])
  graph[b - 1].append([a - 1, v])

def _calc(i):

  q = []
  heapq.heappush(q, [0, i])
  dist = [float('inf') for _ in range(n)]
  dist[i] = 0
  
  while q:

    bd, bi = heapq.heappop(q)

    if dist[bi] < bd:
      continue

    for ni, ed in graph[bi]:
      nd = bd + ed

      if dist[ni] < nd:
        continue

      dist[ni] = nd
      heapq.heappush(q, [nd, ni])

  return sum(items[i] for i in range(n) if dist[i] <= m)

answer = 0
for i in range(n):
  answer = max(_calc(i), answer)
print(answer)