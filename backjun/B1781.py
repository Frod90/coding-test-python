import sys
input = sys.stdin.readline
import heapq

n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]
infos.sort(key=lambda x:(x[0], -x[1]))

q = []
for deadline, count in infos:
  heapq.heappush(q, count)

  while len(q) > deadline:
    heapq.heappop(q)

print(sum(q))