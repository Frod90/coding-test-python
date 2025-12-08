import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dists = [0] * 10_001
for i in range(n):
  for j in range(10_000, costs[i] - 1, -1):
    dists[j] = max(dists[j], dists[j - costs[i]] + memories[i])

for i in range(10_001):
  if dists[i] >= m:
    print(i)
    break