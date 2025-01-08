
n = int(input())
numbers = list(map(int, input().split()))

answers = numbers
answer = numbers[0]

for i in range(n - 1):
  answers[i + 1] = max(answers[i] + answers[i + 1], answers[i + 1])
  answer = max(answer, answers[i + 1])

print(answer)
