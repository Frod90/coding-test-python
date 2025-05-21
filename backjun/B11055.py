
n = int(input())
nums = list(map(int, input().split()))
dist = nums[:]

for i in range(1, n):
  for j in range(i):
    if nums[j] < nums[i]:
      dist[i] = max(dist[i], dist[j] + nums[i])

print(max(dist))