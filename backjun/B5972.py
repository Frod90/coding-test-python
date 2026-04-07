import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
links = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, v = map(int, input().split())
  links[a].append((b, v))
  links[b].append((a, v))

q = []
q.append((0, 1))
INF = n * 1_001
dists = [INF] * (n + 1)
dists[1] = 0

while q:
  before_value, current_node = heapq.heappop(q)

  if dists[current_node] < before_value:
    continue

  for next_node, ev in links[current_node]:
    next_value = before_value + ev
    if next_value < dists[next_node]:
      dists[next_node] = next_value
      heapq.heappush(q, (next_value, next_node))

print(dists[n])