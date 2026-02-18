code = input()

if code[0] == '0':
  print(0)
  exit()

if len(code) == 1:
  print(1)
  exit()

dist = [0] * len(code)
dist[0] = 1
if code[1] != '0':
  dist[1] += 1
if 10 <= int(code[:2]) <= 26:
  dist[1] += 1

for i in range(2, len(code)):

  if code[i] != '0':
    dist[i] = (dist[i] + dist[i - 1]) % 1000000

  if 10 <= int(code[i - 1 : i + 1]) <= 26:
    dist[i] = (dist[i] + dist[i - 2]) % 1000000

print(dist[-1])