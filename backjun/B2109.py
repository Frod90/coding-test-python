import sys
input = sys.stdin.readline
import heapq

n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]
infos.sort(key=lambda x:(x[1], -x[0]))
q = []

for pay, day in infos:
  heapq.heappush(q, pay)

  while len(q) > day:
    heapq.heappop(q)

while len(q) > n:
  heapq.heappop(q)
print(sum(q))