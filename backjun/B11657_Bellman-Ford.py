import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
dists = [float('inf')] * (v + 1)
dists[1] = 0

for _ in range(v - 1):
  for a, b, c in edges:
    if dists[a] != float('inf') and dists[b] > dists[a] + c:
      dists[b] = dists[a] + c

for a, b, c in edges:
  if dists[a] != float('inf') and dists[b] > dists[a] + c:
    print(-1)
    exit()

for i in range(2, v + 1):
  if dists[i] == float('inf'):
    print(-1)
  else:
    print(dists[i])
