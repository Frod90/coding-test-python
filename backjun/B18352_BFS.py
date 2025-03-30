import sys
input = sys.stdin.readline

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

q = deque()
dist = [-1 for _ in range(n + 1)]

q.append(x)
dist[x] = 0

answers = []

while q:
  b = q.popleft()

  if dist[b] > k:
    break

  for nx in graph[b]:
    if dist[nx] == -1:
      dist[nx] = dist[b] + 1
      q.append(nx)

      if dist[nx] == k:
        answers.append(nx)

if len(answers) == 0:
  print(-1)
else:
  answers.sort()
  for answer in answers:
    print(answer)