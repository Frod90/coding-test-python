
n = int(input())

yIndexs = []
indexs = []

for i in range(n):
  x, y = map(int, input().split())
  yIndexs.append(y)
  indexs.append([x, y])

indexs.sort()
hMax = max(yIndexs)

area = 0
tmpX = indexs[0][0]
tmpY = indexs[0][1]
hMaxXs = []
for i in range(n):

  if(tmpY > indexs[i][1]):
    continue

  area += abs(indexs[i][0] -  tmpX) * tmpY
  tmpX = indexs[i][0]
  tmpY = indexs[i][1]

  if(indexs[i][1] == hMax):
    hMaxXs.append(indexs[i][0])
    break

indexs.sort(reverse=True)
tmpX = indexs[0][0]
tmpY = indexs[0][1]
for i in range(n):

  if(tmpY > indexs[i][1]):
    continue

  area += abs(indexs[i][0] -  tmpX) * tmpY
  tmpX = indexs[i][0]
  tmpY = indexs[i][1]

    
  if(indexs[i][1] == hMax):
    hMaxXs.append(indexs[i][0])
    break

maxHArea = (abs(hMaxXs[1] - hMaxXs[0]) + 1) * hMax
print(area + maxHArea)
