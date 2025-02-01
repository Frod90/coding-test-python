
import math

n = int(input())
count = 0

n -= 4
max = math.floor(n / 2)

for i in range(1, max + 1):
  rest = n - 2 * i

  for j in range(math.floor(rest / 2) + 1):
    count += 1

print(count)

