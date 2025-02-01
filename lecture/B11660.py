import sys
input = sys.stdin.readline

n, count = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
sumGraph = [[0 for i in range(n + 1)] for _ in range(n + 1)]

for row in range(1, n + 1):
  for col in range(1, n + 1):
    sumGraph[row][col] = sumGraph[row - 1][col] + sumGraph[row][col - 1] - sumGraph[row - 1][col - 1] + graph[row - 1][col - 1]

for _ in range(count):
  row1, col1, row2, col2 = map(int, input().split())
  answer = sumGraph[row2][col2] - sumGraph[row2][col1 - 1] - sumGraph[row1 - 1][col2] + sumGraph[row1 - 1][col1 - 1]
  print(answer)
