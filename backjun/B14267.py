import sys
input = sys.stdin.readline

n, m = map(int, input().split())
employees = list(map(int, input().split()))
links = [[] for _ in range(n + 1)]
for i, employee in enumerate(employees):
  if employee == -1:
    continue
  links[employee].append(i + 1)

dists = [0] * (n + 1)
for _ in range(m):
  a, v = map(int, input().split())
  dists[a] += v

for current in range(n + 1):
  for next in links[current]:
    dists[next] += dists[current]

print(*dists[1:])