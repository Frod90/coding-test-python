
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

graph.sort(key=lambda x: x[0])

visit = [1]*n

for i in range(n):
  for j in range(i):
    if graph[i][1] > graph[j][1]:
      visit[i] = max(visit[i], visit[j] + 1)

print(n - max(visit))