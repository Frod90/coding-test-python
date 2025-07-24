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
  
  if ranks[parentA] < ranks[parentB]:
    parents[parentA] = parentB
  elif ranks[parentB] > ranks[parentB]:
    parents[parentB] = parentA
  else:
    parents[parentB] = parentA
    ranks[parentA] += 1

  return True

n = int(input())
graph = [list(map(int, input().split())) + [i] for i in range(n)]

parents = [i for i in range(n)]
ranks = [0] * n

x_sort = sorted(graph, key=lambda x:(x[0]))
y_sort = sorted(graph, key=lambda x:(x[1]))
z_sort = sorted(graph, key=lambda x:(x[2]))

edges = []
for i in range(n - 1):
  x, y, z, index = x_sort[i]
  nx, ny, nz, nindex = x_sort[i + 1]
  edges.append([nx - x, index, nindex])

  x, y, z, index = y_sort[i]
  nx, ny, nz, nindex = y_sort[i + 1]
  edges.append([ny - y, index, nindex])

  x, y, z, index = z_sort[i]
  nx, ny, nz, nindex = z_sort[i + 1]
  edges.append([nz - z, index, nindex])

edges.sort()
answer = 0
for value, a, b in edges:
  if union(a, b):
    answer += value
print(answer)