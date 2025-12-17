import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegreed = [0] * (n + 1)
values = [0] * (n + 1)

for i in range(1, n + 1):
  input_info = list(map(int, input().split()))
  values[i] = input_info[0]
  
  for before_node in (input_info[1:-1]):
    graph[before_node].append(i)
    indegreed[i] += 1

answers = [0] * (n + 1)
q = deque()
for i in range(1, n + 1):
  if indegreed[i] == 0:
    q.append(i)
    answers[i] = values[i]

while q:
  now = q.popleft()

  for next_node in graph[now]:
    indegreed[next_node] -= 1
    answers[next_node] = max(answers[next_node], answers[now] + values[next_node])
    if indegreed[next_node] == 0:
      q.append(next_node)

for value in answers[1:]:
  print(value)