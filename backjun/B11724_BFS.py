import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visit = [0 for _ in range(n + 1)]

def bfs(i, count):
  q = deque()
  q.append(i)

  while q:
    b = q.popleft()

    for nb in graph[b]:
      if visit[nb] == 0:
        visit[nb] = count
        q.append(nb)

count = 0
for i in range(1, n + 1):
  if visit[i] == 0:
    count += 1 
    visit[i] = count
    bfs(i, count)

print(max(visit))