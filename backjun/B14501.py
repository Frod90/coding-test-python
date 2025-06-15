import sys

input = sys.stdin.readline

n = int(input())
values = [list(map(int, input().split())) for _ in range(n)]
dists = [0 for _ in range(n + 1)]

for i in range(n):
  dists[i + 1] = max(dists[i], dists[i + 1])

  ei, v = values[i]
  ni = i + ei
  if ni <= n:
    dists[ni] = max(dists[ni], dists[i] + v)

print(dists[-1])