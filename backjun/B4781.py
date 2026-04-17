import sys
input = sys.stdin.readline

while True:
  n, m = map(float, input().split())
  n, m = int(n), int(round(m * 100))
  if n == 0 and m == 0:
    break
  
  infos = []
  for _ in range(n):
    calorie, price = map(float, input().split())
    infos.append((int(calorie), int(round(price * 100))))

  dists = [0] * (m + 1)
  for calorie, price in infos:
    for i in range(price, m + 1):
      dists[i] = max(dists[i], dists[i - price] + calorie)
  print(dists[m])