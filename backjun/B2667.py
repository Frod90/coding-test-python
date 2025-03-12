import sys
sys.setrecursionlimit(99999999)

n = int(input())

graph = []
dist = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
  graph.append(list(map(int, list(input()))))

answers = []
def recur(x, y):
  
  for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    nx, ny = x + dx, y + dy

    if 0 <= nx < n and 0 <= ny < n:
      if graph[ny][nx] == 1 and dist[ny][nx] == 0:

        dist[ny][nx] = idx
        answers[-1] += 1
        recur(nx, ny)

idx = 0
for x in range(n):
  for y in range(n):

    if graph[y][x] == 1 and dist[y][x] == 0:
      idx += 1
      dist[y][x] = idx
      answers.append(1)
      recur(x, y)

print(idx)
answers.sort()
for answer in answers:
  print(answer)