
n = int(input())

flavors = [list(map(int, input().split())) for _ in range(n)]

def recur(i, sour, bit, use):

  global answer

  if i >= n:
    if use > 0:
      answer = min(answer, abs(sour - bit))
    return
  
  recur(i + 1, sour * flavors[i][0], bit + flavors[i][1], use + 1)
  recur(i + 1, sour, bit, use)

answer = 1_000_000_000
recur(0, 1, 0, 0)
print(answer)
