
n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

numbers.sort()

answer = 0
j = 0
for i in range(n)[::-1]:

  if j >= i:
    break
  if numbers[i] >= k:
    continue
  
  while numbers[j] + numbers[i] <= k and j < i:
    if numbers[j] + numbers[i] == k:
      answer += 1
    j += 1

print(answer)
