
N = int(input())
dists = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]

for i in range(1, 10):
  dists[1][i][1 << i] = 1

for length in range(1, N):
  for node in range(10):
    for bit in range(1 << 10):
      if dists[length][node][bit] == 0:
        continue

      if node < 9:
        next_node = node + 1
        next_bit = bit | (1 << (next_node))
        dists[length + 1][next_node][next_bit] += dists[length][node][bit]
        dists[length + 1][next_node][next_bit] %= 1_000_000_000

      if node > 0:
        next_node = node - 1
        next_bit = bit | (1 << next_node)
        dists[length + 1][next_node][next_bit] += dists[length][node][bit]
        dists[length + 1][next_node][next_bit] %= 1_000_000_000

answer = 0
for i in range(10):
  answer = (answer + dists[N][i][(1 << 10) - 1]) % 1_000_000_000
print(answer)