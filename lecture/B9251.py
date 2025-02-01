
string01 = list(str(input()))
string02 = list(str(input()))

w = len(string01)
h = len(string02)

visit = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

for y in range(1, h + 1):
  for x in range(1, w + 1):

    if string01[x - 1] == string02[y - 1]:
      visit[y][x] = visit[y - 1][x - 1] + 1
    else:
      visit[y][x] = max(visit[y - 1][x], visit[y][x - 1])

print(visit[h][w])