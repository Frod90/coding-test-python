
n = int(input())
m = int(input())
wrongNums = list(input()) if m else []

answer = abs(n - 100)

for candidate in range(1_000_000):
  for i in str(candidate):
    if i in wrongNums:
      break
  else:
    answer = min(answer, len(str(candidate)) + abs(n - candidate))

print(answer)