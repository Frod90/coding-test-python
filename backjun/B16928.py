import sys
from collections import deque

input = sys.stdin.readline

graph = [i for i in range(101)]

n, m = map(int, input().split())
for _ in range(n + m):
  a, b = map(int, input().split())
  graph[a] = b

def _cal():

  dist = [0 for _ in range(101)]

  q = deque()
  q.append(1)

  while q:

    bi = q.popleft()

    for ei in range(1, 7):
      ni = bi + ei
      if ni <= 100:
        ni = graph[ni]

        if dist[ni] == 0:
          dist[ni] = dist[bi] + 1
          q.append(ni)
        
  return dist[-1]

print(_cal())        