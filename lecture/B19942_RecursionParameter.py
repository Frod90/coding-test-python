
n = int(input())

_a, _b, _c, _d = map(int, input().split())
ingredients = [list(map(int, input().split())) for _ in range(n)]

def recur(i, a, b, c, d, e):

  global answers, minPay
  
  if a >= _a and b >= _b and c >= _c and d >= _d:
    if minPay > e:
      minPay = e
      answers = indexs.copy()

    return
  
  if i >= n:
    return
  
  indexs.append(i + 1)
  recur(i + 1, a + ingredients[i][0], b + ingredients[i][1], c + ingredients[i][2], d + ingredients[i][3], e + ingredients[i][4])
  indexs.pop()
  recur(i + 1, a, b, c, d, e)

indexs = []
maxPay = 501 * 15
minPay = maxPay
answers = []
recur(0, 0, 0, 0, 0, 0)

if minPay != maxPay:
  print(minPay)
  answers.sort()
  print(*answers)
else:
  print(-1)