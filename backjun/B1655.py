import sys
import heapq
input = sys.stdin.readline

n = int(input())
lower_q = []
upper_q = []

for _ in range(n):
  heapq.heappush(lower_q, -int(input()))

  if upper_q and -lower_q[0] > upper_q[0]:
    to_upper = -heapq.heappop(lower_q)
    to_lower = -heapq.heappop(upper_q)
    heapq.heappush(upper_q, to_upper)
    heapq.heappush(lower_q, to_lower)

  if len(lower_q) - len(upper_q) > 1:
    heapq.heappush(upper_q, -heapq.heappop(lower_q))
  elif len(upper_q) > len(lower_q):
    heapq.heappush(lower_q, -heapq.heappop(upper_q))
  
  print(-lower_q[0])