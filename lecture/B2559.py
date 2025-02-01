
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
for i in range(0, k):
  answer += numbers[i]

sum = answer
for i in range(k, n):
  sum = sum - numbers[i - k] + numbers[i]
  answer = max(answer, sum)

print(answer)
