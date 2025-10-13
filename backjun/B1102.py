import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
status = [True if i == 'Y' else False for i in list(input().rstrip())]
p = int(input())

bit = 0
for i, s in enumerate(status):
  if s:
    bit |= 1 << i
dists = [-1] * (1 << n)

def recur(bit):
  if bin(bit).count('1') >= p:
    return 0
  if dists[bit] != -1:
    return dists[bit]

  dists[bit] = float('inf')

  for i in range(n):
    if (bit & (1 << i)) == 0:
      continue
    
    for j in range(n):
      if i == j:
        continue
      if bit & (1 << j):
        continue
      dist = recur(bit | (1 << j)) + graph[i][j]
      dists[bit] = min(dists[bit], dist)

  return dists[bit]

if p == 0:
  print(0)
elif bit:
  print(recur(bit))
else:
  print(-1)