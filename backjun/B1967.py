import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

links = [[] for _ in range(n + 1)]
for _ in range(n - 1):
  a, b, v = map(int, input().split())
  links[a].append([b, v])
  links[b].append([a, v])

def _cal(i):

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
  for i in range(n + 1):
    if dists[i] > maxi:
      idx, maxi = i, dists[i]
  return idx, maxi

tmpIdx, _ = _cal(1)
_, answer = _cal(tmpIdx)

print(answer)