import sys
input = sys.stdin.readline
sys.setrecursionlimit(100_001)

def _find(a):
  if a == parents[a]:
    return a
  
  parents[a] = _find(parents[a])
  return parents[a]

def _union(a, b):
  parentA, parentB = _find(a), _find(b)
  if parentA == parentB:
    return False
  
  if ranks[parentA] > ranks[parentB]:
    parents[parentB] = parentA
  elif ranks[parentB] > ranks[parentA]:
    parents[parentA] = parentB
  else:
    parents[parentA] = parentB
    ranks[parentB] += 1
  
  return True

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])
parents = [i for i in range(n + 1)]
ranks = [0] * (n + 1)

answer = 0
count = 1
last = 0
for a, b, v in edges:
  if _union(a, b):
    answer += v
    last = v
    count += 1

    if count >= n:
      break

print(answer - last)