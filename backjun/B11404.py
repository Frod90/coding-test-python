import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

maxi = float('inf')
graph = [[maxi for _ in range(n)] for _ in range(n)]

for _ in range(m):
  a, b, v = map(int, input().split())
  graph[a - 1][b - 1] = min(graph[a - 1][b - 1], v)

for i in range(n):
  graph[i][i] = 0

for k in range(n):
  for y in range(n):
    for x in range(n):
        graph[y][x] = min(graph[y][x], graph[y][k] + graph[k][x])

for y in range(n):
  for x in range(n):
    if graph[y][x] == maxi:
      print(0, end=" ")
    else:
      print(graph[y][x], end=" ")
  print()