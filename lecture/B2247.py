
number = int(input())

answer = 0
for i in range(2, int(number**0.5) + 1):
  div = number // i
  answer += i * (div - i + 1) + (div * (div + 1) // 2) - (i * (i + 1) // 2)

print(answer % 1_000_000)