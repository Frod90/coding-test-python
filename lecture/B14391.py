import sys
input = sys.stdin.readline

h, w = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(h)]

answer = 0
for bit in range(1 << (h * w)):
  total_sum = 0

  for i in range(h):
    row_sum = 0
    for j in range(w):
      index = w * i + j
      if bit & (1 << index) == 0:
        row_sum = row_sum * 10 + graph[i][j]
      else:
        total_sum += row_sum
        row_sum = 0
    total_sum += row_sum

  for i in range(w):
    col_sum = 0
    for j in range(h):
      index = w * j + i
      if bit & (1 << index):
        col_sum = col_sum * 10 + graph[j][i]
      else:
        total_sum += col_sum
        col_sum = 0
    total_sum += col_sum

  answer = max(answer, total_sum)

print(answer)