
n = int(input())
nums = list(map(int, input().split()))

dist = [1 for _ in range(n)]
for i in range(n):
  for j in range(i):
    if nums[j] > nums[i]:
      dist[i] = max(dist[j] + 1, dist[i])

print(max(dist))