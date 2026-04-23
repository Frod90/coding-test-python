import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = float('inf')
graph = [[INF] * (n + 1) for _ in range(n + 1)]
routes = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b, v = map(int, input().split())
  if v < graph[a][b]:
    graph[a][b] = v
    routes[a][b] = b
for i in range(1, n + 1):
  graph[i][i] = 0

for k in range(1, n + 1):
  for y in range(1, n + 1):
    for x in range(1, n + 1):
      if graph[y][k] + graph[k][x] < graph[y][x]:
        graph[y][x] = graph[y][k] + graph[k][x]
        routes[y][x] = routes[y][k]

for y in range(1, n + 1):
  row = [graph[y][x] if graph[y][x] != INF else 0 for x in range(1, n + 1)]
  print(*row)

for start_node in range(1, n + 1):
  for target_node in range(1, n + 1):
    if routes[start_node][target_node] == 0:
      print(0)
      continue
    
    route = [start_node]
    current_node = start_node
    while current_node != target_node:
      current_node = routes[current_node][target_node]
      route.append(current_node)
    print(*[len(route)] + route)
