import sys

input = sys.stdin.readline

dists = [1, 2]
maxi = 2**31
i = 1
while dists[-1] < maxi:
  i += 1
  dists.append(dists[-1] + i)
  dists.append(dists[-1] + i)

t = int(input())

for _ in range(t):
  s, e = map(int, input().split())
  n = e - s

  for i in range(len(dists)):
    if n <= dists[i]:
      print(i + 1)
      break