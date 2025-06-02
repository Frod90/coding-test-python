import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
js = [list(map(int, input().split())) for _ in range(n)]
bs = [int(input()) for _ in range(k)]
js.sort()
bs.sort()

q = []
ji = 0
answer = 0

for b in bs:

  while ji < n and js[ji][0] <= b:
    heapq.heappush(q, -js[ji][1])
    ji += 1

  if q:
    answer -= heapq.heappop(q)

print(answer)