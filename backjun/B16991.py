import sys
input = sys.stdin.readline

n = int(input())
positions = [list(map(int, input().split())) for _ in range(n)]
dists = [[-1] * (1 << n) for _ in range(n)]

def recur(node, bit):
  if bit == (1 << n) - 1:
    x0, y0 = positions[0]
    x1, y1 = positions[node]
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5
  
  if dists[node][bit] != -1:
    return dists[node][bit]
  
  dists[node][bit] = float('inf')
  cx, cy = positions[node]

  for next_node in range(1, n):
    if node == next_node:
      continue
    if bit & (1 << next_node):
      continue

    nx, ny = positions[next_node]
    dist = recur(next_node, bit | (1 << next_node)) + ((cx - nx)**2 + (cy - ny)**2)**0.5
    dists[node][bit] = min(dists[node][bit], dist)

  return dists[node][bit]

print(recur(0, 1))