from collections import deque

n = int(input())
linkCount = int(input())

graph = [[] for i in range(n + 1)]

for i in range(linkCount):
  a, b = map(int, input().split())
  
  graph[a].append(b)
  graph[b].append(a)

visit = [0] * (n + 1)

q = deque()
q.append(1)
visit[1] = 1

answer = 0

while q:
  a = q.popleft()

  for i in graph[a]:
    if visit[i] == 0:
      q.append(i)
      visit[i] = 1
      answer += 1

print(answer)