
n, x = map(int, input().split())
volumnes = list(map(int, input().split()))

volumnes.sort()
answer = 0

i = 0
j = len(volumnes) - 1
add = x / 2
rests = 0
while i <= j:

  if volumnes[i] == x:
    answer += 1
    i += 1
    continue
  if volumnes[j] == x:
    answer += 1
    j -= 1
    continue

  if i == j:
    rests += 1
    break

  tmp = volumnes[i] + volumnes[j]

  if tmp >= add:
    answer += 1
    i += 1
    j -= 1
  elif tmp < add:
    rests += 1
    i += 1

print(answer + rests // 3)