import sys
input = sys.stdin.readline

n = int(input())
times = [0] * n
pays = [0] * n

for i in range(n):
  t, p = map(int, input().split())
  times[i], pays[i] = t, p

dists = [0] * (n + 1)
tmp = 0
for i in range(n):
  t, p = times[i], pays[i]
  if dists[i + 1] < dists[i]:
    dists[i + 1] = dists[i]

  if i + t <= n:
    dists[i + t] = max(dists[i + t], dists[i] + p)

print(max(dists))