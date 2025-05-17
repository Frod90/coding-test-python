
n = int(input())

nums = [1 for _ in range(10)]
answers = nums[:]


for i in range(n - 1):
  for j in range(10):
    for k in range(j + 1, 10):
      answers[k] += nums[j]

  nums = answers[:]

print(sum(nums) % 10007)