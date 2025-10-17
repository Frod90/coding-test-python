import sys
sys.setrecursionlimit(100000)

def recur(length, node, bit):
  if length == n:
    if bit == (1 << 10) - 1:
      return 1
    return 0

  if dists[length][node][bit] != -1:
    return dists[length][node][bit]
  
  value = 0
  if node < 9:
    value += recur(length + 1, node + 1, bit | (1 << (node + 1)))
  if node > 0:
    value += recur(length + 1, node - 1, bit | (1 << (node - 1)))
  
  dists[length][node][bit] = value % 1_000_000_000
  return dists[length][node][bit]

n = int(input())
dists = [[[-1] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]

answer = 0
for i in range(1, 10):
  answer += recur(1, i, 1 << i)
  answer %= 1_000_000_000
print(answer)
