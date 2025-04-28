nums = [True for _ in range(10_001)]

for i in range(2, 101):

  if nums[i]:
    for j in range(i * i, 10_001, i):
      nums[j] = False

t = int(input())

for _ in range(t):
  n = int(input())

  num = n // 2
  while not nums[num] or not nums[n - num]:
    num -= 1
  print(num, n - num)