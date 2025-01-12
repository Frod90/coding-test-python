
n = int(input())

ds = []
gs = []
ts = []
bs = []
ms = []
_d, _g, _t, _b = map(int, input().split())
for _ in range(n):
  d, g, t, b, m = map(int, input().split())
  ds.append(d)
  gs.append(g)
  ts.append(t)
  bs.append(b)
  ms.append(m)

maxMoney = 501 * n
arr = []
answers = []
moneys = [maxMoney]
def recur(i, j):

  if i == n:
    return
  
  for k in range(j + 1, n + 1):

    arr.append(k)

    d, g, t, b, m = 0, 0, 0, 0, 0
    for index in arr:
      d += ds[index - 1]
      g += gs[index - 1]
      t += ts[index - 1]
      b += bs[index - 1]
      m += ms[index - 1]

    if d >= _d and g >= _g and t >= _t and b >= _b:
      tmp = arr.copy()
      answers.append(tmp)
      moneys.append(m)

    recur(i + 1, k)
    arr.pop()

recur(0, 0)

minMoney = min(moneys)

if minMoney != maxMoney:
  print(minMoney)
  for i in range(len(moneys)):
    if moneys[i] == minMoney:
      print(*answers[i - 1])
      break
else:
  print(-1)