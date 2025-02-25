
n = int(input())
heights = list(map(int, input().split()))
dist = [0] * n

for i in range(len(dist)):

  count = 0

  j = i
  xDist = 0
  beforeRate = -1_000_000_000

  while(j > 0):

    xDist += 1
    j -= 1

    rate = (heights[j] - heights[i]) / xDist
    if rate > beforeRate:
      count += 1
      beforeRate = rate

  xDist = 0
  beforeRate = -1_000_000_000

  for j in range(i + 1, len(heights)):

    xDist += 1
    rate = (heights[j] - heights[i]) / xDist
    
    if rate > beforeRate:
      count += 1
      beforeRate = rate

  dist[i] = count

print(dist)