n, k = map(int, input().split())
mod = 1_000_000_007

answer = 1
for i in range(n, n - k, -1):
  answer = (answer * i) % mod

division = 1
for i in range(1, k + 1):
  division = (division * i) % mod

answer = answer * pow(division, mod - 2, mod) % mod
print(answer)