import sys
input = sys.stdin.readline

maxi = 10_001
dists = [0] * (maxi)
dists[0] = 1

for i in range(1, 4):
  for j in range(i, maxi):
    dists[j] += dists[j - i]

t = int(input())
for _ in range(t):
  n = int(input())
  print(dists[n])