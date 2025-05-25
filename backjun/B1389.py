import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [set() for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].add(b)
  graph[b].add(a)

def _bfs(sn):

  dist = [-1 for _ in range(n + 1)]
  dist[sn] = 0
  q = deque()
  q.append(sn)

  while q:
    bn = q.popleft()

    for nn in graph[bn]:
      if dist[nn] == -1:
        dist[nn] = dist[bn] + 1
        q.append(nn)

  return sum(d for d in dist[1:] if d != -1)

answer = 0
cal = float('inf')
for i in range(1, n + 1):
  tmp = _bfs(i)
  if tmp < cal:
    cal = tmp
    answer = i

print(answer)