from collections import deque

n, k = map(int, input().split())

def bfs(n, k):

  if n >= k:
    return n - k

  maxi = 20
  dist = [-1 for _ in range(maxi)]
  q = deque()
  q.append(n)
  dist[n] = 0

  while q:
    x = q.popleft()

    if x == k:
      return dist[x]

    if x * 2 < maxi:
      if dist[x * 2] == -1:
        dist[x * 2] = dist[x]
        q.appendleft(x * 2)

    for nx in [x - 1, x + 1]:
      if 0 <= nx < maxi:
        if dist[nx] == -1:
          dist[nx] = dist[x] + 1
          q.append(nx)

print(bfs(n, k))