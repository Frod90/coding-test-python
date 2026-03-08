import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pre = [[] for _ in range(n)]
suf = [[] for _ in range(n)]

for _ in range(m):
  a, b = map(int, input().split())
  pre[b - 1].append(a - 1)
  suf[a - 1].append(b - 1)
  
def recur(graph, current, route, visit):
  
  for next in graph[current]:
    if not visit[next]:
      visit[next] = True
      route.add(next)
      recur(graph, next, route, visit)

answer = 0
for node in range(n):
  route = set()
  route.add(node)
  visit = [False] * n
  visit[node] = True
  recur(pre, node, route, visit)

  visit = [False] * n
  visit[node] = True
  recur(suf, node, route, visit)

  if len(route) == n:
    answer += 1

print(answer)