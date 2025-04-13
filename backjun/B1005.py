import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):

  n, k = map(int, input().split())
  values = list(map(int, input().split()))
  degrees = [0 for _ in range(n + 1)]

  graph = [[] for _ in range(n + 1)]
  for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    degrees[b] += 1

  e = int(input())

  q = []
  for i in range(1, n + 1):
    if degrees[i] == 0:
      heapq.heappush(q, [values[i - 1], i])

  while q:
    bv, b = heapq.heappop(q)

    if b == e:
      print(bv)
      break

    for nb in graph[b]:
      degrees[nb] -= 1
      if degrees[nb] == 0:
        heapq.heappush(q, [bv + values[nb - 1], nb])