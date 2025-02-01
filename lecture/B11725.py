from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = deque()
q.append(1)
answers = [0] * (n + 1)
answers[1] = 1 

while q:

  parent = q.popleft()

  for child in graph[parent]:
    if not answers[child]:
      answers[child] = parent
      q.append(child)

for i in range(2, n + 1):
  print(answers[i])