
n = int(input())
nums = list(map(int, input().split()))
dist = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(i, n + 1):
    dist[j] = max(dist[j], dist[j - i] + nums[i - 1])

print(dist[-1])