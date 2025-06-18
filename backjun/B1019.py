
n = int(input())
dists = [0 for _ in range(10)]

digit = 1
while n >= digit:
  higher = n // (digit * 10)
  current = (n - higher * digit * 10) // digit
  lower = n % digit

  for i in range(10):
    if i < current:
      dists[i] += (higher + 1) * digit
    elif i == current:
      dists[i] += higher * digit + lower + 1
    else:
      dists[i] += higher * digit

  dists[0] -= digit
  digit *= 10

print(*dists)