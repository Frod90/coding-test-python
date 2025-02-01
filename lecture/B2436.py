
g, l = map(int, input().split())

def _gcd(a, b):
  
  while(b % a != 0):

    gap = b % a
    b = a
    a = gap

  return a

def _lcm(a, b):
  return a * b // g

max = g * l

answer = [g, l]
for i in range(g, int(max**0.5) + 1, g):
  j = max // i

  # print(i, j)
  if(g == _gcd(i, j)):
    if(l == _lcm(i, j)):
      if(i + j < answer[0] + answer[1]):
        answer = [i, j]

print(*answer)