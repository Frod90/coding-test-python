import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
links = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
times = [0] * (n + 1)
for node in range(1, n + 1):
  info = list(map(int, input().split()))
  times[node] = info[0]
  degree[node] = info[1]
  for j in range(2, len(info)):
    links[info[j]].append(node)

dists = [0] * (n + 1)
q = deque()
for node in range(1, n + 1):
  if degree[node] == 0:
    q.append(node)
    dists[node] = times[node]

while q:
  current = q.popleft()

  for next in links[current]:
    degree[next] -= 1
    dists[next] = max(dists[current] + times[next], dists[next])
    
    if degree[next] == 0:
      q.append(next)

print(max(dists))