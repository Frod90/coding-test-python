
n, r, c = map(int, input().split())
leng = 2**n

def recur(x, y, bv, degree, count):

  if degree == n:
    print(count)
    return

  ev = bv // 2

  if c < x + ev:
    if r < y + ev:
      recur(x, y, ev, degree + 1, count)
    else:
      recur(x, y + ev, ev, degree + 1, count + ev * bv)
  else:
    if r < y + ev:
      recur(x + ev, y, ev, degree + 1, count + ev**2)
    else:
      recur(x + ev, y + ev, ev, degree + 1, count + ev * bv + ev**2)

recur(0, 0, leng, 0, 0)
