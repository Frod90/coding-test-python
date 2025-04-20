import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
  
  a = int(input())

  if a == 0:
    if q:
      ab, bv = heapq.heappop(q)
      print(bv)
    else:
      print(0)
  else:
    heapq.heappush(q, [abs(a), a])