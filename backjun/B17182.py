import sys
input = sys.stdin.readline

def recur(node, bit):
  if bit == (1 << n) - 1:
    return 0
  
  if dists[node][bit] != -1:
    return dists[node][bit]

  dists[node][bit] = float('inf')
  for next_node in range(n):
    if node == next_node:
      continue
    if bit & (1 << next_node):
      continue

    dist = recur(next_node, bit | (1 << next_node)) + graph[node][next_node]
    dists[node][bit] = min(dists[node][bit], dist)

  return dists[node][bit]

n, s = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
  for y in range(n):
    for x in range(n):
      graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

dists = [[-1] * (1 << n) for _ in range(n)]
print(recur(s, (1 << s)))