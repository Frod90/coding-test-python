import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

links = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, v = map(int, input().split())
  links[a].append((b, v))
  links[b].append((a, v))

visit = [False] * (n + 1)
q = [(0, 1)]
count = 0
answer = 0

while q:
  bv, current = heapq.heappop(q)
  if count == n:
    break
  
  if not visit[current]:
    visit[current] = True
    answer += bv
    count += 1

    for next, nv in links[current]:
      if not visit[next]:
        heapq.heappush(q, (nv, next))

print(answer)