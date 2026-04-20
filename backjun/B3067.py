import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  coins = list(map(int, input().split()))
  target = int(input())

  dists = [0] * (target + 1)
  dists[0] = 1
  for coin in coins:
    for i in range(coin, target + 1):
      dists[i] += dists[i - coin]
  print(dists[target])