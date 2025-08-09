import sys
input = sys.stdin.readline

s01 = list(input().rstrip())
s02 = list(input().rstrip())

w, h = len(s01), len(s02)
dists = [[[0, ""] for _ in range(w + 1)] for _ in range(h + 1)]

for y in range(1, h + 1):
  for x in range(1, w + 1):
    if s02[y - 1] == s01[x - 1]:
      dists[y][x][0] = dists[y - 1][x - 1][0] + 1
      dists[y][x][1] = dists[y - 1][x - 1][1] + s01[x - 1]
    else:
      if dists[y - 1][x][0] > dists[y][x - 1][0]:
        dists[y][x][0] = dists[y - 1][x][0]
        dists[y][x][1] = dists[y - 1][x][1]
      else:
        dists[y][x][0] = dists[y][x - 1][0]
        dists[y][x][1] = dists[y][x - 1][1]

count, string = dists[-1][-1]
print(count)
print(string)