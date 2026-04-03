import sys
input = sys.stdin.readline

t, w = map(int, input().split())
infos = [int(input()) - 1 for _ in range(t)]

dists = [[0] * (w + 1) for _ in range(t + 1)]

for time in range(1, t + 1):
  tree = infos[time - 1]
  
  value = 1 if tree == 0 else 0
  dists[time][0] = dists[time - 1][0] + value
  for move in range(1, w + 1):
    value = 1 if tree == move % 2 else 0
    dists[time][move] = max(dists[time - 1][move - 1], dists[time - 1][move]) + value

print(max(dists[t]))