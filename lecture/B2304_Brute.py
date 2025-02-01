
n = int(input())

xIndexs = []
yIndexs = []

for _ in range(n):
  x, y = map(int, input().split())
  xIndexs.append(x)
  yIndexs.append(y)

area = 0
hMax = max(yIndexs)
xMin = min(xIndexs)
xMax = max(xIndexs)

for h in range(1, hMax + 1):
  
  tmpXMin = xMax
  tmpXMax = xMin

  for j in range(n):
    if yIndexs[j] >= h:
      tmpXMin = min(tmpXMin, xIndexs[j])
      tmpXMax = max(tmpXMax, xIndexs[j])

  area += tmpXMax - tmpXMin + 1

print(area)
