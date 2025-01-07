
a, b = map(int, input().split())

def _f(number):
  sum = number
  for i in range(1, 50):
    sum += (number // 2**i)*(2**i - 2**(i - 1))

  return sum

print(_f(b) - _f(a - 1))
