import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

links = [[] for _ in range(n + 1)]
for _ in range(n):
  inputs = list(map(int, input().split()))
  for i in range(1, len(inputs) - 2, 2):
    links[inputs[0]].append((inputs[i], inputs[i + 1]))


visit = [False for _ in range(n + 1)]

def _bfs(i):
  dists = [-1 for _ in range(n + 1)]
  
  q = deque()
  q.append(i)
  dists[i] = 0

  while q:
    bi = q.popleft()

    for ni, v in links[bi]:
      if dists[ni] == -1:
        dists[ni] = dists[bi] + v
        q.append(ni)

  idx, maxi = 0, 0
  for i in range(1, n + 1):
    if dists[i] > maxi:
      idx, maxi = i, dists[i]

  return idx, maxi

idx, maxi = _bfs(1)
idx, maxi = _bfs(idx)
print(maxi)