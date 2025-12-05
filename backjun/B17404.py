
import sys
input = sys.stdin.readline

def cal(start_index):
  dists = [[0] * 3 for _ in range(n)]
  dists[0][start_index] = graph[0][start_index]
  dists[0][(start_index + 1) % 3] = float('inf')
  dists[0][(start_index + 2) % 3] = float('inf')

  for i in range(1, n - 1):
    for j in range(3):
      dists[i][j] = min(dists[i - 1][(j + 1) % 3], dists[i - 1][(j + 2) % 3]) + graph[i][j]

  for j in range(3):
    if j == start_index:
      dists[-1][j] = float('inf')
      continue
    
    dists[-1][j] = min(dists[-2][(j + 1) % 3], dists[-2][(j + 2) % 3]) + graph[-1][j]

  return min(dists[-1])

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')
for start_index in range(3):
  answer = min(answer, cal(start_index))
print(answer)