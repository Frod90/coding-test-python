import sys
input = sys.stdin.readline

def w(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1

  if a > 20 or b > 20 or c > 20:
    return 1048576

  if a < b and b < c:
    if (a, b, c) in d:
      return d[(a, b, c)]
    
    result = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    d[(a, b, c)] = result
    return result

  if (a, b, c) in d:
    return d[(a, b, c)]

  result = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
  d[(a, b, c)] = result
  return result

d = dict()
while True:
  a, b, c = map(int, input().split())

  if a == -1 and b == -1 and c == -1:
    break

  result = w(a, b, c)
  print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(result))