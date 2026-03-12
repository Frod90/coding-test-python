import sys
input = sys.stdin.readline

n = int(input())
nodes = [list(map(float, input().split())) for _ in range(n)]

edges = []
for i in range(n):
  ax, ay = nodes[i]
  
  for j in range(i + 1, n):
    bx, by = nodes[j]
    v = ((ax - bx)**2 + (ay - by)**2)**0.5
    edges.append((i, j, v))

parents = [i for i in range(n)]
ranks = [0] * n

def find(a):
  if parents[a] == a:
    return a
  
  parents[a] = find(parents[a])
  return parents[a]

def union(a, b):
  parentA, parentB = find(a), find(b)
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

edges.sort(key=lambda x:x[2])
answer = 0
for a, b, v in edges:
  if union(a, b):
    answer += v
print(answer)