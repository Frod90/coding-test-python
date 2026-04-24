import sys
input = sys.stdin.readline
import heapq

n = int(input())
edges = []
for _ in range(n):
  a, b = map(int, input().split())
  if a < b:
    edges.append((a, b))
  else:
    edges.append((b, a))
d = int(input())

edges.sort(key=lambda x:(x[1], x[0]))
q = []
answer = 0

for a, b in edges:
  if b - a > d:
    continue
  
  heapq.heappush(q, a)
  start = b - d
  while q and q[0] < start:
    heapq.heappop(q)
  answer = max(answer, len(q))

print(answer)