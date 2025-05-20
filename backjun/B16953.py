
a, b = map(int, input().split())

tmp = b
count = 0
while True:

  count += 1

  if tmp <= a:
    if tmp != a:
      count = -1
    break

  if tmp % 10 == 1:
    li = list(str(tmp))
    li.pop()
    tmp = int("".join(li))
  elif tmp % 2 == 0:
    tmp = tmp // 2
  else:
    count = -1
    break

print(count)