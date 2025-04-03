import sys
input = sys.stdin.readline

n = int(input())
parents = [i for i in range(n + 1)]
ranks = [0 for _ in range(n + 1)]

def _find(i):

  if i == parents[i]:
    return i
  
  parents[i] = _find(parents[i])
  return parents[i]

def _union(a, b):

  parentA, parentB = _find(a), _find(b)
  if parentA == parentB:
    return
  
  if ranks[parentA] < ranks[parentB]:
    parents[parentA] = parentB
  elif ranks[parentB] < ranks[parentA]:
    parents[parentB] = parentA
  elif ranks[parentA] == ranks[parentB]:
    parents[parentA] = parentB
    ranks[parentB] += 1

m = int(input())
for i in range(n):
  arr = list(map(int, input().split()))

  for j in range(n):
    if arr[j] == 1:
      _union(i + 1, j + 1)

routes = list(map(int, input().split()))
parent = _find(routes[0])
isAnswer = True
for route in routes:
  if _find(route) != parent:
    isAnswer = False
    break

if isAnswer:
  print("YES")
else:
  print("NO")