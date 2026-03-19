import sys
input = sys.stdin.readline

a, b = map(int, input().split())
maxi = int(b**0.5)
net = [True] * (maxi + 1)
net[0], net[1] = False, False
primes = []

for num in range(2, maxi + 1):
  if net[num]:
    primes.append(num)

    for next in range(num * num, maxi + 1, num):
      net[next] = False

answer = 0
for prime in primes:
  tmp = prime**2
  while tmp <= b:
    if tmp >= a:
      answer += 1
    tmp *= prime

print(answer)