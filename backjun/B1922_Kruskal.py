import sys
input = sys.stdin.readline

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

n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x:x[2])

parents = [i for i in range(n + 1)]
ranks = [0] * (n + 1)

answer = 0
for a, b, v in edges:
  if union(a, b):
    answer += v
print(answer)