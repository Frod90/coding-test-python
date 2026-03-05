import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
  n = int(input())
  info = list(map(int, input().split()))
  links = [[False] * (n + 1) for _ in range(n + 1)]
  degree = [0] * (n + 1)
  for i in range(len(info)):
    for j in range(i + 1, len(info)):
      links[info[i]][info[j]] = True
    degree[info[i]] = i

  m = int(input())
  for _ in range(m):
    a, b = map(int, input().split())

    if links[a][b]:
      links[b][a] = True
      links[a][b] = False
      degree[a] += 1
      degree[b] -= 1
    else:
      links[a][b] = True
      links[b][a] = False
      degree[b] += 1
      degree[a] -= 1

  q = deque()
  for i in range(1, n + 1):
    if degree[i] == 0:
      q.append(i)

  answer = []
  is_multi = False
  while q:
    if len(q) > 1:
      is_multi = True
      break

    current = q.popleft()
    answer.append(current)

    for i in range(1, n + 1):
      if i == current:
        continue

      if links[current][i]:
        degree[i] -= 1
        if degree[i] == 0:
          q.append(i)
        
  if is_multi:
    print("?")
  elif len(answer) != n:
    print("IMPOSSIBLE")
  else:
    print(*answer)