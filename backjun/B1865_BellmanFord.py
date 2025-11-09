import sys
input = sys.stdin.readline

def hasNegativeCircle(n, edges):
  maxi = float('inf')
  dists = [maxi] * (n + 1)
  dists[0] = 0

  for _ in range(n - 1):
    for a, b, v in edges:
      if dists[a] != maxi and dists[a] + v < dists[b]:
        dists[b] = dists[a] + v

  for a, b, v in edges:
    if dists[a] != maxi and dists[a] + v < dists[b]:
      return True
  return False

t = int(input())
for _ in range(t):
  n, m, w = map(int, input().split())
  edges = []
  for i in range(1, n + 1):
    edges.append([0, i, 0])

  for _ in range(m):
    a, b, v = map(int, input().split())
    edges.append([a, b, v])
    edges.append([b, a, v])
  
  for _ in range(w):
    a, b, v = map(int, input().split())
    edges.append([a, b, -v])

  if hasNegativeCircle(n, edges):
    print("YES")
  else:
    print("NO")