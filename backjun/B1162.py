import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
links = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, v = map(int, input().split())
  links[a].append([v, b])
  links[b].append([v, a])

dist = [[float('inf')] * (k + 1) for _ in range(n + 1)]
for i in range(k + 1):
  dist[1][i] = 0
q = [[0, 1, 0]]

while q:
  v, bi, c = heapq.heappop(q)

  if v > dist[bi][c]:
    continue

  for ev, ni in links[bi]:
    if c < k and dist[ni][c + 1] > v:
      dist[ni][c + 1] = v
      heapq.heappush(q, [v, ni, c + 1])

    nv = v + ev
    if dist[ni][c] > nv:
      dist[ni][c] = nv
      heapq.heappush(q, [nv, ni, c])

print(min(dist[-1]))