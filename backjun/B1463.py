from collections import deque

n = int(input())
dist = [0] * 1_000_001

q = deque()
q.append(n)

while q:

  before = q.popleft()

  if before == 1:
    break

  count = dist[before] + 1

  a, b, c = before // 3, before // 2, before - 1

  if before % 3 == 0 and dist[a] == 0:
    dist[a] = count
    q.append(a)

  if before % 2 == 0 and dist[b] == 0:
    dist[b] = count
    q.append(b)

  if dist[c] == 0:
    dist[c] = count
    q.append(c)

print(dist[1])