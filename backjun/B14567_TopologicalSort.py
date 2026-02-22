import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
links = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  links[a].append(b)
  degree[b] += 1

ranks = [1] * (n + 1)

q = deque()
for i in range(1, n + 1):
  if degree[i] == 0:
    q.append(i)

while q:
  current = q.popleft()

  for next in links[current]:
    degree[next] -= 1

    if degree[next] == 0:
      ranks[next] = max(ranks[current] + 1, ranks[next])
      q.append(next)

print(*ranks[1:])