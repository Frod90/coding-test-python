import sys
input = sys.stdin.readline

n = int(input())
a, b, c, d, e, f = list(map(int, input().split()))

if n == 1:
  print(sum([a, b, c, d, e, f]) - max(a, b, c, d, e, f))
  exit()

one_side = min(a, b, c, d, e, f)
two_side = min(
  a + b, a + c, a + d, a + e,
  b + c, b + d, b + f,
  c + e, c + f,
  d + e, d + f,
  e + f
  )
three_side = min(
  a + b + c, a + b + d, a + d + e, a + c + e,
  f + b + c, f + b + d, f + d + e, f + c + e
)

one_side_count = (n - 2) * (n - 1) * 4 + (n - 2) * (n - 2)
two_side_count = (n - 1) * 4 + (n - 2) * 4
three_side_count = 4

answer = one_side * one_side_count + two_side * two_side_count + three_side * three_side_count
print(answer)