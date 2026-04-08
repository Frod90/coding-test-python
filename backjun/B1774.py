import sys
input = sys.stdin.readline

def _find(a):
  if a == parents[a]:
    return a
  
  parents[a] = _find(parents[a])
  return parents[a]

def _union(a, b):
  parent_a, parent_b = _find(a), _find(b)
  if parent_a == parent_b:
    return False
  
  if ranks[parent_a] < ranks[parent_b]:
    parents[parent_a] = parent_b
  elif ranks[parent_b] < ranks[parent_a]:
    parents[parent_b] = parent_a
  else:
    parents[parent_b] = parent_a
    ranks[parent_a] += 1

  return True

n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]

parents = [node for node in range(n)]
ranks = [0] * n

for _ in range(m):
  a, b = map(int, input().split())
  _union(a - 1, b - 1)

edges = []
for current in range(n):
  current_x, current_y = points[current]
  for next in range(current + 1, n):
    next_x, next_y = points[next]
    edges.append((current, next, (abs(current_x - next_x)**2 + abs(current_y - next_y)**2)**0.5))

count = 1
dist = 0

edges.sort(key=lambda x:x[2])
for a, b, v in edges:
  if count >= n:
    break
  
  if _union(a, b):
    dist += v
    count += 1

print(f"{dist:.2f}")