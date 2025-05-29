from collections import deque

n = int(input())
links = list(map(int, input().split()))
tar = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
  if links[i] != -1:
    graph[links[i]].append(i)

answer = sum(1 for a in graph if not a)

if len(graph[links[tar]]) == 1:
  answer += 1

q = deque()
q.append(tar)

while q:

  bn = q.popleft()

  if not graph[bn]:
    answer -= 1
    continue

  for nn in graph[bn]:
    q.append(nn)

print(answer)