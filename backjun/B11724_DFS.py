import sys
input = sys.stdin.readline

sys.setrecursionlimit(9999999)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visit = [0 for _ in range(n + 1)]

def recur(s, count):

  for ns in graph[s]:
    if visit[ns] == 0:
      visit[ns] = count
      recur(ns, count)

count = 0
for i in range(1, n + 1):
  if visit[i] == 0:
    count += 1
    visit[i] = count
    recur(i, count)

print(max(visit))