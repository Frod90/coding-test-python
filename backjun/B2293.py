import sys

sys.setrecursionlimit(99999999)
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
dist = [0 for _ in range(k + 1)]
dist[0] = 1

for coin in coins:
  for i in range(coin, k + 1):
    dist[i] += dist[i - coin]

print(dist[k])