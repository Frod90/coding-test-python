import sys
input = sys.stdin.readline

sys.setrecursionlimit(99999999)

from collections import deque

n, m, v = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visit = [0 for _ in range(n + 1)]
answers = []

def dfs(node):
  
  answers.append(node)
  visit[node] = 1

  graph[node].sort()
  for next in graph[node]:
    if visit[next] == 0:
      dfs(next)

dfs(v)
print(*answers)

visit = [0 for _ in range(n + 1)]
answers = []

def bfs(node):

  q = deque()
  q.append(node)
  visit[node] = 1
  answers.append(node)

  while q:
    before = q.popleft()

    for next in graph[before]:
      if visit[next] == 0:
        q.append(next)
        visit[next] = 1
        answers.append(next)

bfs(v)
print(*answers)