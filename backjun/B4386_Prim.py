import sys
input = sys.stdin.readline
import heapq

n = int(input())
nodes = [list(map(float, input().split())) for _ in range(n)]

links = [[] for _ in range(n)]
for i in range(n):
  ax, ay = nodes[i]
  
  for j in range(i + 1, n):
    bx, by = nodes[j]
    v = ((ax - bx)**2 + (ay - by)**2)**0.5
    links[i].append((j, v))
    links[j].append((i, v))

q = [(0, 0)]
visit = [False] * n
count = 0
answer = 0
while q:
  if count == n:
    break

  bv, current = heapq.heappop(q)
  if not visit[current]:
    visit[current] = True
    answer += bv
    count += 1

    for next, nv in links[current]:
      if not visit[next]:
        heapq.heappush(q, (nv, next))

print(answer)