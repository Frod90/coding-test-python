import sys
sys.setrecursionlimit(99999999)

input = sys.stdin.readline

n, m = map(int, input().split())

parents = [i for i in range(n + 1)]
ranks = [0]*(n + 1)


def _find(a):

  if parents[a] == a:
    return a
  
  parents[a] = _find(parents[a])
  return parents[a]


def _union(a, b):

  parentA, parentB = _find(a), _find(b)

  if parentA == parentB:
    return

  rankA, rankB = ranks[parentA], ranks[parentB]

  if rankA == rankB:
    parents[parentB] = parentA
    ranks[parentA] += 1
  elif rankA > rankB:
    parents[parentB] = parentA
  else:
    parents[parentA] = parentB


for _ in range(m):
  f, a, b = map(int, input().split())

  if f == 1:
    
    if _find(a) == _find(b):
      print("YES")
    else:
      print("NO")

  if f == 0:
    _union(a, b)
