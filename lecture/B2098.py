import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
maxi = 10**8
dists = [[-1] * (1 << n) for _ in range(n)]

def recur(node, visit):
  if visit == (1 << n) - 1:
    if graph[node][0] == 0:
      return maxi
    return graph[node][0]
  
  if dists[node][visit] != -1:
    return dists[node][visit]

  dists[node][visit] = maxi
  for i in range(n):
    if graph[node][i] == 0:
      continue
    if visit & (1 << i):
      continue

    dist = recur(i, visit | (1 << i)) + graph[node][i]
    dists[node][visit] = min(dists[node][visit], dist)

  return dists[node][visit]

print(recur(0, 1))