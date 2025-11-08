from collections import deque

n = int(input())
dists = [[-1, -1] for _ in range(n + 1)]
dists[n] = [0, 0]
q = deque()
q.append(n)

while q and q[0]> 1:
  before_node = q.popleft()

  if before_node % 3 == 0:
    next_node = before_node // 3
    if dists[next_node][0] == -1:
      dists[next_node] = [dists[before_node][0] + 1, before_node]
      q.append(next_node)

  if before_node % 2 == 0:
    next_node = before_node // 2
    if dists[next_node][0] == -1:
      dists[next_node] = [dists[before_node][0] + 1, before_node]
      q.append(next_node)

  next_node = before_node - 1
  if dists[next_node][0] == -1:
    dists[next_node] = [dists[before_node][0] + 1, before_node]
    q.append(next_node)

route = [1]
node = 1
while node != n:
  node = dists[node][1]
  route.append(node)

print(dists[1][0])
print(*route[::-1])