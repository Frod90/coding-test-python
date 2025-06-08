import sys

input = sys.stdin.readline

c, n = map(int, input().split())
maxi = float('inf')
dist = [float('inf') for _ in range(c + 101)]
dist[0] = 0

for _ in range(n):
  a, b = map(int, input().split())

  for i in range(b, c + 101):
    dist[i] = min(dist[i], dist[i - b] + a)

print(min(dist[c:]))