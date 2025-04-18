a, b, c = map(int, input().split())

def _recur(a, b, c):

  if b == 1:
    return a % c

  tmp = _recur(a, b // 2, c)

  if b % 2 == 1:
    return a * tmp**2 % c
  else:
    return tmp**2 % c

print(_recur(a, b, c))