import sys
input = sys.stdin.readline
import heapq

n = int(input())
q = []

for _ in range(n):
  heapq.heappush(q, int(input()))

for _ in range(n):
  print(heapq.heappop(q))
