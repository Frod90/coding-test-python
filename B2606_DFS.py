n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visit = [0]*(n + 1)

def recur(i):

  visit[i] = 1

  for next in graph[i]:
    if visit[next]:
      continue

    recur(next)

recur(1)
print(sum(visit) - 1)

