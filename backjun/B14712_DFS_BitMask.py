
h, w = map(int, input().split())

def recur(x, y, cur, pre):
  global answer
  
  if y == h:
    answer += 1
    return

  if x == w - 1:
    recur(0, y + 1, 0, cur)
  else:
    recur(x + 1, y, cur, pre)

  if x >= 1 and y >= 1:
    up = pre & (1 << x)
    left = cur & (1 << (x - 1))
    up_left = pre & (1 << (x - 1))

    if up and left and up_left:
      return
  
  next_cur = cur | (1 << x)
  if x == w - 1:
    recur(0, y + 1, 0, next_cur)
  else:
    recur(x + 1, y, next_cur, pre)

answer = 0
recur(0, 0, 0, 0)
print(answer)