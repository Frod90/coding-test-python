import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
homes = []
chickens = []

for j in range(n):
  graph = list(map(int, input().split()))

  for i in range(n):
    if graph[i] == 1:
      homes.append([i, j])
    elif graph[i] == 2:
      chickens.append([i, j])

def _calc(combi):

  result = 0
  for hx, hy in homes:    
    result += min(abs(hx - cx) + abs(hy - cy) for cx, cy in combi)

  return result

answer = float('inf')
for combi in combinations(chickens, m):
  answer = min(answer, _calc(combi))

print(answer)