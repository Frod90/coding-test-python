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
graph = [list(map(int, input().split())) for _ in range(n)]
edges = []
for a in range(n):
  for b in range(a + 1, n):
    edges.append((a, b, graph[a][b]))
edges.sort(key=lambda x:x[2])

parents = [i for i in range(n)]
ranks = [0] * n

count = 1
answer = 0
for a, b, v in edges:
  if union(a, b):
    answer += v
    count += 1

  if count == n:
    break

print(answer)