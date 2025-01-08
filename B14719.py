
h, w = map(int, input().split())
heights = list(map(int, input().split()))

hMax = max(heights)

area = 0
hMaxXIndexs = []

tmpY = heights[0]
tmpX = 0
for i in range(1, w):
  
  if(tmpY > heights[i]):
    continue

  area += (i - tmpX) * tmpY
  tmpY = heights[i]
  tmpX = i

  if(tmpY >= hMax):
    hMaxXIndexs.append(i)
    break

tmpY = heights[w - 1]
tmpX = w - 1
for i in range(w - 1, 0, -1):
  
  if(tmpY > heights[i]):
    continue

  area += abs(i - tmpX) * tmpY
  tmpY = heights[i]
  tmpX = i

  if(tmpY >= hMax):
    hMaxXIndexs.append(i)
    break

area += (max(hMaxXIndexs) - min(hMaxXIndexs) + 1) * hMax
print(area - sum(heights))