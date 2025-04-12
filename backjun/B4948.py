import sys
input = sys.stdin.readline

maxi = 123456 * 2
dist = [1 for _ in range(maxi + 1)]
dist[1] = 0

for i in range(2, int(maxi**0.5) + 1):

  if dist[i] == 0:
    continue

  for j in range(i * 2, maxi + 1, i):
    dist[j] = 0

for i in range(2, len(dist)):
  dist[i] += dist[i - 1]

while True:

  n = int(input())
  if n == 0:
    break

  print(dist[2 * n] - dist[n])