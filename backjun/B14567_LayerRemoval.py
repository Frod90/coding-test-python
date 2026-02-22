import sys
input = sys.stdin.readline

n, m = map(int, input().split())
links = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
degree[0] = -1
for _ in range(m):
  a, b = map(int, input().split())
  links[a].append(b)
  degree[b] += 1

ranks = [0] * (n + 1)
ranks[0] = -1
count = 1
is_continue = True
while is_continue:
  is_continue = False

  for node in range(n, 0, -1):
    if degree[node] == 0:
      degree[node] = -1
      ranks[node] = count
      for next in links[node]:
        degree[next] -= 1
      is_continue = True

  count += 1

print(*ranks[1:])