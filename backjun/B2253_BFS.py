import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
invalid_nodes = set(int(input()) for _ in range(m))
visit = [set() for _ in range(n + 1)]

q = deque()
start_node = 2
if start_node not in invalid_nodes:
  visit[start_node].add(1)
  q.append((start_node, 1, 1))

while q:
  current_node, current_dist, count = q.popleft()
  next_count = count + 1

  if current_node == n:
    print(count)
    exit()

  for ev in range(-1, 2):
    next_dist = current_dist + ev

    if next_dist > 0:
      next_node = current_node + next_dist
      if next_node <= n and next_node not in invalid_nodes and next_dist not in visit[next_node]:
        visit[next_node].add(next_dist)
        q.append((next_node, next_dist, next_count))

print(-1)