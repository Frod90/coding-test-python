import sys
input = sys.stdin.readline

n, k = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dists = [-INF] * (k + 1)

for i in range(n):
  work, work_value, cycle, cycle_value = infos[i]
  if i == 0:
    dists[0] = 0
  else:
    dists[0] = -INF

  for i in range(k, 0, -1):
    candidate1, candidate2 = -INF, -INF
    if i >= work:
      candidate1 = dists[i - work] + work_value
    if i >= cycle:
      candidate2 = dists[i - cycle] + cycle_value
    
    dists[i] = max(candidate1, candidate2)
    
print(max(dists))