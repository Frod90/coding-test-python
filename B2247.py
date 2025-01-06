
number = int(input())

answer = 0
for i in range(2, number):
  count = int(number / i) - 1
  answer = answer + i * count

print(int(answer % 1_000_000))