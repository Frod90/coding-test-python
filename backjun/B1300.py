n = int(input())
k = int(input())

left, right = 1, n**2
answer = 0
while left <= right:
  mid = (left + right) // 2

  count = 0
  for i in range(1, n + 1):
    count += min(mid // i, n)

  if count < k:
    left = mid + 1
  else:
    answer = mid
    right = mid - 1

print(answer)