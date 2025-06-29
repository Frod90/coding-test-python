import sys
sys.setrecursionlimit(99999999)
input = sys.stdin.readline

n = int(input())
log = 21

graph = [[] for _ in range(n + 1)]
parents = [[0] * log for _ in range(n + 1)]
depths = [0] * (n + 1)

for _ in range(n - 1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def _recur(c, p):
  parents[c][0] = p
  depths[c] = depths[p] + 1

  for v in graph[c]:
    if v != p:
      _recur(v, c)

_recur(1, 0)

for d in range(1, log):
  for i in range(1, n + 1):
    parents[i][d] = parents[parents[i][d - 1]][d - 1]

def _find(a, b):
  if depths[a] < depths[b]:
    a, b = b, a
  
  diff = depths[a] - depths[b]
  for d in range(log - 1, -1, -1):
    if diff & (1 << d):
      a = parents[a][d]
  
  if a == b:
    return a
  
  for d in range(log - 1, -1, -1):
    if parents[a][d] != parents[b][d]:
      a, b = parents[a][d], parents[b][d]

  return parents[a][0]

m = int(input())
for _ in range(m):
  a, b = map(int, input().split())
  print(_find(a, b))