import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def find(a):
  if a == parents[a]:
    return a
  
  parents[a] = find(parents[a])
  return parents[a]

def union(a, b):
  parentA, parentB = find(a), find(b)
  if parentA == parentB:
    return False

  if ranks[parentA] > ranks[parentB]:
    parents[parentB] = parentA
  elif ranks[parentA] < ranks[parentB]:
    parents[parentA] = parentB
  else:
    parents[parentA] = parentB
    ranks[parentB] += 1

  return True

while True:
  n, m = map(int, input().split())
  if n == 0 and m == 0:
    break

  parents = [i for i in range(n)]
  ranks = [0] * n

  edges = [list(map(int, input().split())) for _ in range(m)]
  edges.sort(key=lambda x:x[2])
  answer = 0
  count = 0
  for a, b, v in edges:
    if union(a, b):
      answer += v
      count += 1
    
    if count == n:
      break

  total = 0
  for _, _, v in edges:
    total += v

  print(total - answer)