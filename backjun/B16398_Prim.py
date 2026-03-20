import sys
input = sys.stdin.readline
import heapq

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

q = [(0, 0)]
visit = [False] * n
count = 0
answer = 0

while q and count < n:
  cv, current = heapq.heappop(q)

  if not visit[current]:
    visit[current] = True
    count += 1
    answer += cv

    for next in range(n):
      if current == next:
        continue

      if not visit[next]:
        heapq.heappush(q, (graph[current][next], next))

print(answer)