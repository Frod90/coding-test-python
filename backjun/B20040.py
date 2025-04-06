import sys
input = sys.stdin.readline

sys.setrecursionlimit(99999999)

n, m = map(int, input().split())
parents = [i for i in range(n)]
ranks = [0 for _ in range(n)]
inputs = [list(map(int, input().split())) for _ in range(m)]

def _find(a):

  if a == parents[a]:
    return a

  parents[a] = _find(parents[a])
  return parents[a]

def _union(parentA, parentB):
  
  if ranks[parentA] < ranks[parentB]:
    parents[parentA] = parentB
  elif ranks[parentB] < ranks[parentA]:
    parents[parentB] = parentA
  else:
    parents[parentB] = parentA
    ranks[parentA] += 1

def _isCycle(parentA, parentB):
    
    if parentA == parentB:
      return True
    return False

answer = 0
for i in range(m):
  a, b = inputs[i]
  parentA, parentB = _find(a), _find(b)

  if _isCycle(parentA, parentB):
    answer = i + 1
    break

  _union(parentA, parentB)
  
print(answer)