
n, m = map(int, input().split())
nums = list(map(int, input().split()))

rests = [0 for _ in range(m)]
prefix_sum = 0

for num in nums:
  prefix_sum += num
  rests[prefix_sum % m] += 1

count = rests[0]
for rest in rests:
  count += rest * (rest - 1) // 2

print(count)