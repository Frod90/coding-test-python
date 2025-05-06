import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
  for y in range(n):
    for x in range(n):
      if graph[y][k] == 1 and graph[k][x] == 1:
        graph[y][x] = 1

for row in graph:
  print(*row)