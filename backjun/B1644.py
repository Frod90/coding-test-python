n = int(input())

prime = []
candidates = [True] * (n + 1)
candidates[0], candidates[1] = False, False

for num in range(2, n + 1):
  if not candidates[num]:
    continue
  
  prime.append(num)
  for notCandidage in range(num * 2, n + 1, num):
    candidates[notCandidage] = False

length = len(prime)
left, right = 0, 0
tmpSum = 0
count = 0
while right < length:
  tmpSum += prime[right]
  right += 1

  while left < length and tmpSum > n:
    tmpSum -= prime[left]
    left += 1

  if tmpSum == n:
    count += 1

print(count)