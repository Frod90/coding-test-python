import sys
input = sys.stdin.readline

import heapq

V, E = map(int, input().split())

visit = [0] * (V + 1)
links = [[] for _ in range(V + 1)]

for _ in range(E):
  a, b, c = list(map(int, input().split()))
  links[a].append([b, c])
  links[b].append([a, c])

q = []
heapq.heappush(q, [0, 1])

count = 0
answer = 0

while q:

  if count == V:
    break

  beforeValue, base = heapq.heappop(q)

  if visit[base] == 0:
    answer += beforeValue
    visit[base] = 1
    count += 1

    for next, value in links[base]:
      heapq.heappush(q, [value, next])

print(answer)