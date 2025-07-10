import sys
sys.setrecursionlimit(99999999)
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def multi(a, b):
  r = [[0] * len(b[0]) for _ in range(len(a))]

  for i in range(len(r)):
    for j in range(len(r[0])):
      for k in range(len(b)):
        r[i][j] += a[i][k] * b[k][j]
        r[i][j] %= 1_000

  return r

def _recur(i):
  if i == 1:
    return [[x % 1_000 for x in row] for row in graph]
  
  r = _recur(i // 2)
  r = multi(r, r)
  
  if i % 2 == 1:
    r = multi(r, graph)
  
  return r

for row in _recur(k):
  print(*row)