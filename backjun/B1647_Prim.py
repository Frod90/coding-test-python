import sys
input = sys.stdin.readline
import heapq


n, m = map(int, input().split())
links = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b, v = map(int, input().split())
  links[a].append((b, v))
  links[b].append((a, v))

q = []
heapq.heappush(q, (0, 1))
answer = 0
last = 0
count = 0
visit = [False] * (n + 1)

while q:
  if count == n:
    break
  
  bv, current = heapq.heappop(q)

  if not visit[current]:
    answer += bv
    count += 1
    last = max(last, bv)
    visit[current] = True

    for next, nv in links[current]:
      if not visit[next]:
        heapq.heappush(q, (nv, next))

print(answer - last)