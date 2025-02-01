
n = int(input())

heights = [0]*1001
yIndexs = []
xIndexs = []

for _ in range(n):
  x, y = map(int, input().split())
  heights[x] = y
  xIndexs.append(x)
  yIndexs.append(y)

hMax = max(yIndexs)
lMax = max(xIndexs)
lMin = max(xIndexs)
hMaxXIndexs = []

area = 0
tmpH = 0
for i in range(lMin, lMax + 1):

  if heights[i] == hMax:
    hMaxXIndexs.append(i)
    break

  if heights[i] > tmpH:
    tmpH = heights[i]

  area += tmpH

tmpH = 0
for i in range(lMax, lMin - 1, -1):

  if heights[i] == hMax:
    hMaxXIndexs.append(i)
    break

  if heights[i] > tmpH:
    tmpH = heights[i]

  area += tmpH

print(hMax, hMaxXIndexs)
area += (max(hMaxXIndexs) - min(hMaxXIndexs) + 1) * hMax
print(area)