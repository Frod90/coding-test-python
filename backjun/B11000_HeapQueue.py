import sys
import heapq
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort()

q = []
for s, e in times:
  if q and q[0] <= s:
    heapq.heappop(q)
  heapq.heappush(q, e)

print(len(q))