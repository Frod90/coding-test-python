
target = int(input())

fiveCount = target // 5
answer = -1

while fiveCount >= 0:
  rest = target - fiveCount * 5

  if rest % 3 == 0:
    answer = fiveCount + rest // 3
    break

  fiveCount -= 1

print(answer)