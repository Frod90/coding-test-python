import sys
input = sys.stdin.readline
from collections import deque

def cal(n, k):
  maxi = 200_001
  dists = [-1] * maxi
  dists[n] = n
  q = deque([n])

  while q:
    now = q.popleft()
    if now + 1 == k or now - 1 == k or now * 2 == k:
      dists[k] = now
      break

    for next_node in [now + 1, now - 1, now * 2]:
      if 0 <= next_node < maxi:
        if dists[next_node] == -1:
          dists[next_node] = now
          q.append(next_node)

  route = [k]
  index = k
  while index != n:
    route.append(dists[index])
    index = dists[index]
  return route

n, k = map(int, input().split())
route = cal(n, k)
print(len(route) - 1)
print(*route[::-1])