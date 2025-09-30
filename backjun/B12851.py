from collections import deque

n, k = map(int, input().split())
maxi = max(n, k) * 2 + 1

graph = [[float('inf'), 0] for _ in range(maxi)]
graph[n][0] = 0
graph[n][1] = 1
q = deque([n])

while q:
  bi = q.popleft()
  if bi == k:
    break

  v = graph[bi][0]
  routes = graph[bi][1]
  if bi + 1 < maxi:
    if graph[bi + 1][0] > v + 1:
      graph[bi + 1][0] = v + 1
      graph[bi + 1][1] += routes
      q.append(bi + 1)
    elif graph[bi + 1][0] == v + 1:
      graph[bi + 1][1] += routes
  
  if bi - 1 >= 0:
    if graph[bi - 1][0] > v + 1:
      graph[bi - 1][0] = v + 1
      graph[bi - 1][1] += routes
      q.append(bi - 1)
    elif graph[bi - 1][0] == v + 1:
      graph[bi - 1][1] += routes
  
  if bi * 2 < maxi:
    if graph[bi * 2][0] > v + 1:
      graph[bi * 2][0] = v + 1
      graph[bi * 2][1] += routes
      q.append(bi * 2)
    elif graph[bi * 2][0] == v + 1:
      graph[bi * 2][1] += routes

print(graph[k][0])
print(graph[k][1])