
a, b, c, d, e, f = map(int, input().split())

if(a < 0):
  a = -a
  b = -b
  c = -c

if(d < 0):
  d = -d
  e = -e
  f = -f

y = (d * c - a * f) / (d * b - a * e)

if(a == 0):
  x = (f - e * y) / d
else :
  x = (c - b * y) / a

print(str(int(x)) + " " + str(int(y)))