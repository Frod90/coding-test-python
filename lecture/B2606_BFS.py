import sys
input = sys.stdin.readline
# import queue
from collections import deque

n = int(input())
count = int(input())

graph = [[] for _ in range(n + 1)]
visit = [0]*(n + 1)

for _ in range(count):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = deque()
q.append(1)

while q:
  tmp  = q.popleft()
  visit[tmp] = 1

  for a in graph[tmp]:
    if visit[a] == 0:
      q.append(a)

print(sum(visit) - 1)
