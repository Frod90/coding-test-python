import sys
input = sys.stdin.readline

n, m = map(int, input().split())
invalid_nodes = set(int(input()) for _ in range(m))

max_jump, node = 1, 2
count = 1
while node <= n:
  max_jump += 1
  node += max_jump

INF = float('inf')
dists = [[INF] * (max_jump + 1) for _ in range(n + 1)]
start_node = 2
if start_node not in invalid_nodes:
  dists[start_node][1] = 1

for node in range(2, n + 1):
  if node in invalid_nodes:
    continue

  for jump in range(1, max_jump + 1):
    if dists[node][jump] == INF:
      continue

    for ev in range(-1, 2):
      next_jump = jump + ev
      if next_jump == 0 or next_jump > max_jump:
        continue

      next_node = node + next_jump
      if next_node > n:
        continue

      dists[next_node][next_jump] = min(dists[next_node][next_jump], dists[node][jump] + 1)

answer = min(dists[n])
print(answer if answer != INF else -1)