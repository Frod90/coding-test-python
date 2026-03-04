import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
links = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)

for _ in range(m):
  info = list(map(int, input().split()))
  if info[0] == 1:
    continue
  for i in range(1, info[0]):
    links[info[i]].append(info[i + 1])
    degree[info[i + 1]] += 1

answer = []
q = deque()
for i in range(1, n + 1):
  if degree[i] == 0:
    answer.append(i)
    q.append(i)

while q:
  current = q.popleft()

  for next in links[current]:
    degree[next] -= 1
    if degree[next] == 0:
      q.append(next)
      answer.append(next)

if len(answer) == n:
  for a in answer:
    print(a)
else:
  print(0)